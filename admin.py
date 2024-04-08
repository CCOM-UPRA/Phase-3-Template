import os
from functools import wraps
from datetime import datetime, timedelta
from flask import Flask, render_template, redirect, request, session, url_for
from backend_controller.loginController import *
from werkzeug.utils import secure_filename
from backend_controller.ordersController import *
from backend_controller.productsController import *
from backend_controller.accountsController import *
from backend_controller.reportsController import *
from backend_controller.profileController import *

# In this template, you will usually find functions with comments tying them to a specific controller
# admin.py accesses the backend folders
# Every controller accesses its relevant model and will send the information back to this Flask app

app = Flask(__name__, template_folder='backend/')
app.secret_key = 'akeythatissecret'

def login_required(f):
    # This function is utilized to determine whether the user is logged in and can access the routes where
    # this function is added.
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin' not in session:
            session['request'] = request.url
            return redirect(url_for('enterpage', message='mustlogin'))  # Redirect to login page if session variable is not set
        return f(*args, **kwargs)
    return decorated_function

@app.route("/", defaults={'message': None})
@app.route("/<message>")
def enterpage(message):
    return render_template('login (2).html', message=message)


@app.route("/clear")
def clear():
    # Clear session information
    session.clear()
    return redirect("/")


@app.route("/login", methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    # POINTER: loginModel creates a session['admin'] instead
    # Always advisable to name your frontend and backend sessions differently to not cause errors via lingering sessions
    return logincontroller(email=email, password=password)

@app.route("/change/<email>")
@login_required
def change(email):
    # An optional function for students to hash a specific password
    # changePass function can be found in profileController
    # Access this function by typing the word 'change' after your Flask url
    # http://127.0.0.1:5000/change
    changePass(email)
    return render_template("login (2).html")



@app.route("/profile")
@login_required
def profile():
    admin = getUser(3)
    return render_template("profile.html", user1=admin)


@app.route("/editinfo", methods=["POST"])
@login_required
def editinfo():
    # make changes to profile info
    # not implemented in this phase
    return redirect("/profile")


@app.route("/password")
@login_required
def password():
    # FOR STUDENTS TO IMPLEMENT
    return render_template("change-password.html")


@app.route("/products")
@login_required
def products():
    productsp = getProducts()
    return render_template("products.html", products=productsp)


@app.route("/product/<prod>")
@login_required
def product(prod):
    return redirect(url_for('single_product', prodID=prod))


@app.route("/single_product/<prodID>")
@login_required
def single_product(prodID):
    # Return product page for single product selected
    # FOR STUDENTS TO IMPLEMENT
    # ONLY SHOWS RESULTS WITH FIRST TWO DRONE PRODUCTS
    product = getsingleproduct(prodID)
    print("The product: ", product)
    return render_template("single_product.html", prod=product)


@app.route("/editproduct", methods=['POST'])
@login_required
def editproduct():
    # FOR STUDENTS TO IMPLEMENT
    # Process product edits

    # Redirect us to the products list again
    return redirect('/products')


@app.route("/addproduct/", defaults={'message': None})
@app.route("/addproduct/<message>")
@login_required
def addproduct(message):
    # Enter the add product page, will show a message sent from createproduct() once a product is created.
    return render_template("add_product.html", message=message)


@app.route("/createproduct", methods=['POST'])
@login_required
def createproduct():
    # Receive data from add_product.html
    name = request.form.get('name')
    print("name: ", name)
    brand = request.form.get('brand')
    video_res = request.form.get('video_res')

    if 'yes' in request.form:
        wifi = 'Yes'
    else:
        wifi = 'No'

    color = request.form.get('color')
    price = request.form.get('price')
    cost = request.form.get('cost')
    stock = request.form.get('stock')

    # Photo is received from a file and will save the file into your product-images folder
    img = request.files['myfile']
    img2 = img
    filename = secure_filename(img.filename)
    # Adjust to your directory
    # WARNING: Can cause issues if filename has spaces
    current_directory = os.getcwd()
    img.save(os.path.join(current_directory, "static", "images", "product-images", filename))


    if 'active' in request.form:
        status = 'active'
    else:
        status = 'inactive'

    # -> productsController.py
    createNewProduct(name, brand, video_res, wifi, color, price, cost, stock, img2.filename, status)

    # Send message back to html page that product has been added
    message = 'added'
    return render_template("add_product.html", message=message)


@app.route("/accounts/<userType>")
@login_required
def accounts(userType):
    # Retrieve all accounts from 'database' and redirect us to accounts page
    acc = getaccounts(userType)
    return render_template("accounts.html", accounts=acc, userType=userType)


@app.route("/createaccount")
@login_required
def createaccount():
    # Redirect us to account creation page
    # FOR STUDENTS TO IMPLEMENT
    return render_template("create_account.html")


@app.route("/editaccount/<acc>/<userType>")
@login_required
def editaccount(acc, userType):
    # Fetch account given via url and then enter the edit page for that account
    # acc = customer or admin ID

    message = ""


    # Check if updateaccount() sent us a message of form completion to display
    if 'message' in request.args:
        message = request.args.get('message')

    # -> accountsController.py
    account = getaccount(acc, userType)
    print("Account ID: ", acc)
    print("UserType: ", userType)
    return render_template("single_account.html", account=account, userType=userType, message=message)


@app.route("/updateaccount", methods=['POST'])
@login_required
def updateaccount():
    id = request.form.get('id')
    userType = request.form.get('userType')
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    phone_number = request.form.get('pnumber')
    status = request.form.get('status')
    print("STATUS RECEIVED: ", status)

    userInfo = ({'fname': fname, 'lname': lname, 'phone_num': phone_number, 'status': status})
    # Our user info will depend on whether we're updating an admin or customer
    # -> accountsController.py
    updateAccountController(userInfo, userType, id)

    # Go back to edit page with message
    return redirect(url_for('editaccount', acc=id, userType=userType, message='added'))



@app.route("/orders")
@login_required
def orders():
    # Fetches all the orders found in the 'database' to bring to orders page
    all_orders = ordersController()  # -> ordersController.py
    return render_template("orders.html", orders=all_orders)


@app.route("/orders_filter", methods=['POST'])
@login_required
def orders_filter():

    # If search has been sent with info
    if "order_search" in request.form and request.form.get('order_search') != "":
        search = request.form.get('order_search')
        if search.isdigit():  # If string is numeric, search for order via order_id
            searchType = 'order'
        else:  # If string is not numeric, search for orders from a customer via their email
            searchType = 'customer'

        # -> ordersController.py
        orders = filterOrder(search, searchType)
        return render_template("orders.html", orders=orders)
    else:
        # Return full list of orders if search bar is empty
        return redirect("/orders")


@app.route('/editorder/<order>')
@login_required
def editorder(order):
    # TO BE IMPLEMENTED BY STUDENTS
    # ORDER ID IS CURRENTLY A STATIC 1 SET IN THE HTML. MUST BE CHANGED TO REFLECT DYNAMIC CONNECTION TO DB
    # Receive from orders page an order via its id -> order
    # Fetch the products in that order
    orderProducts = getorderproducts(order)
    # Fetch the order itself. Overwrite order as the ID alone is no longer needed
    order = getorder(order)
    # Go to separate page for that order
    return render_template('order.html', products=orderProducts, order=order)


@app.route("/reports")
@login_required
def reports():
    # Fetch the reports page
    products = getProducts()
    return render_template("reports.html", products=products)


@app.route("/product_report", methods=['POST'])
@login_required
def product_report():
    # Function for Single Product Sales Report
    # All Products Sales and Inventory Reports are for STUDENTS TO IMPLEMENT
    product = request.form.get('products')
    if "report_month" in request.form:
        month = request.form.get('report_month')
        timeframe = "Month"
        start_date = month + "-01"   # Add start and end dates for query
        end_date = month + "-31"

        # -> reportsController.py
        orders = getReport(timeframe, start_date, end_date, product)

        # Date to show in title of page
        date = month

    elif "report_week" in request.form:
        timeframe = "Week"
        week = request.form.get('report_week')
        start_date = datetime.strptime(week + '-1', "%Y-W%W-%w")
        end_date = start_date + timedelta(days=6)

        # -> reportsController.py
        orders = getReport(timeframe, start_date, end_date, product)
        start_date = start_date.strftime('%Y/%m/%d')
        end_date = end_date.strftime('%Y/%m/%d')

        # Date to show in title of page
        date = str(start_date) + " - " + str(end_date)

    elif "report_day" in request.form:
        timeframe = "Day"
        start_date = request.form.get('report_day')
        end_date = ""

        # -> reportsController.py
        orders = getReport(timeframe, start_date, end_date, product)

        # Date to show in title of page
        date = start_date

    # Calculate total ($ paid per order) and earnings = (price - cost) * quantity
    total = 0
    earnings = 0
    for order in orders:
        total += float(order['total_price'])

        # Earnings part of order added in model
        earnings += float(order['earnings'])

    # Timeframe: "Day", "Week", "Month"
    # product: product name for the HTML page to show
    # date: the range of dates used in the report for the HTML page to show
    # For results: Day = [X8C Venture on May 7, 2022], Week = [Tello Drone on May 9-15, 2022], Month = [Bebop 2 on May 2022]
    return render_template("single_product_report.html", orders=orders,
                           timeframe=timeframe, date=date, total=total, earnings=earnings, product=product)



@app.route("/report", methods=['POST'])
@login_required
def report():
    # FOR STUDENTS TO IMPLEMENT (ALL PRODUCT SALES REPORT AND STOCK REPORT)
    # IMPORTANT: SALES REPORT MUST REFLECT THE EARNINGS BETWEEN PRODUCT COST AND PRICE ACCORDING TO THE ORDER SALES
    # Initialize variables to use
    date_report = {}
    stock_report = {}
    total = 0

    # If we're going for any of the reports that have a date, get the information and save in date_report
    # All cases give the same results in this case, no matter your date or product input
    if 'report_day' in request.form:
        date_report = getDatedReport()
    if 'report_week' in request.form:
        date_report = getDatedReport()
    if 'report_month' in request.form:
        date_report = getDatedReport()

    # If we're going for the inventory/stock report, get the data and save in stock_report
    if 'stock_report' in request.form:
        stock_report = getStockReport()

    # If we're going for any of the reports with dates, we need a total at the end
    # Calculate the total according to the sum of the total_prices for each item in the report
    if date_report != {}:
        for key, order in date_report.items():
            total += order['total_price']

    # We send to the report page all variables whether empty or not
    # The HTML will validate which variable is empty and will show the appropriate information
    return render_template("report.html", date_report=date_report, stock_report=stock_report, total=total)


# Press the green button in the gutter to run the script.
if __name__ == '__admin__':
    app.run(debug=True)
