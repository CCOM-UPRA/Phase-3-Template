from backend_model.profileModel import MagerDicts
from backend_model.connectDB import *

# ORDER 1
# ------------------------------------------------------------
#
orderDict1 = {"1": {
    "tracking_num": "71287249",
    "order_date": "01/17/23",
    "arrival_date": "01/20/23",
    "address_line_1": "Vista Azulin Calle 11 L13",
    "address_line_2": "Arecibor Puerto Ricor, 00614",
    "total": 755.00,
    "payment_method": "Mastercard",
    'status': 'delivered'
}}

# ORDER 2
# ------------------------------------------------------------
#
orderDict2 = {'2': {
    "tracking_num": "71287249",
    "order_date": "01/17/23",
    "arrival_date": "01/20/23",
    "address_line_1": "Vista Azulin Calle 11 L13",
    "address_line_2": "Arecibor Puerto Ricor, 00614",
    "total": 755.00,
    "payment_method": "Mastercard",
    'status': 'shipped'

}}

# ORDER 3
# ------------------------------------------------------------
#
orderDict3 = {'3': {
    "tracking_num": "71287249",
    "order_date": "01/17/23",
    "arrival_date": "01/20/23",
    "address_line_1": "Vista Azulin Calle 11 L13",
    "address_line_2": "Arecibor Puerto Ricor, 00614",
    "total": 356.00,
    "payment_method": "Mastercard",
    'status': 'processed'
}}

# ORDER 4
# ------------------------------------------------------------
#
orderDict4 = {'4': {
    "tracking_num": "71287249",
    "order_date": "01/17/23",
    "arrival_date": "01/20/23",
    "address_line_1": "Vista Azulin Calle 11 L13",
    "address_line_2": "Arecibor Puerto Ricor, 00614",
    "total": 399.00,
    "payment_method": "Mastercard",
    'status': 'cancelled'
}}



# PRODUCTS
# ------------------------------------------------------------
productDict1 = {"1": {
    "image": 'ruko_f11_pro.jpg',
    "name": 'F11 Pro',
    "brand": 'Ruko',
    "price": 399.00,
    "quantity": 1,
    "total_price": 399.00,
    "order_id": '1'
}}

productDict2 = {"2": {
    "image": 'dji_tello.jpg',
    "name": 'Tello Drone',
    "brand": 'DJI',
    "price": 89.00,
    "quantity": 2,
    "total_price": 178.00,
    "order_id": '1'
}}

productDict3 = {"3": {
    "image": 'dji_tello.jpg',
    "name": 'Tello Drone',
    "brand": 'DJI',
    "price": 89.00,
    "quantity": 2,
    "total_price": 178.00,
    "order_id": '3'
}}

productDict4 = {"4": {
    "image": 'dji_tello.jpg',
    "name": 'Tello Drone',
    "brand": 'DJI',
    "price": 89.00,
    "quantity": 2,
    "total_price": 178.00,
    "order_id": '2'
}}

productDict5 = {"5": {
    "image": 'ruko_f11_pro.jpg',
    "name": 'F11 Pro',
    "brand": 'Ruko',
    "price": 399.00,
    "quantity": 1,
    "total_price": 399.00,
    "order_id": '4'
}}

productDict6 = {"6": {
    "image": 'ruko_f11_pro.jpg',
    "name": 'F11 Pro',
    "brand": 'Ruko',
    "price": 399.00,
    "quantity": 1,
    "total_price": 399.00,
    "order_id": '2'
}}


ordersList = MagerDicts(orderDict1, orderDict2)
ordersList = MagerDicts(ordersList, orderDict3)
ordersList = MagerDicts(ordersList, orderDict4)

productsList = MagerDicts(productDict1, productDict2)
productsList = MagerDicts(productsList, productDict3)
productsList = MagerDicts(productsList, productDict4)
productsList = MagerDicts(productsList, productDict5)
productsList = MagerDicts(productsList, productDict6)


def ordersModel():
    # DB credentials found in backend_model/connectDB.py
    db = Dbconnect()
    orders = []
    query = "SELECT * FROM orders NATURAL JOIN customer"
    ordersFound = db.select(query)
    for o in ordersFound:
        query2 = "SELECT * FROM orders NATURAL JOIN contains WHERE order_id = %s"
        containsFound = db.select(query2, (o['order_id']))
        total_price = 0
        for c in containsFound:
            total_price += round(c['p_price'] * c['product_quantity'], 2)
        orders.append({"id": o['order_id'], "c_id": o['c_id'], "email": o['c_email'], "tracking": o['tracking_number'], "transaction":
                       o['transaction_number'], "order_date": o['order_date'], "arrival_date": o['arrival_date'],
                       "ship_date": o['ship_date'], "total_price": total_price, "status": o['order_status']})
    return orders


def filterOrdersModel(search, searchType):
    # DB credentials found in backend_model/connectDB.py
    db = Dbconnect()
    orders = []
    customer_id = ''
    ordersFound = []
    if searchType == "customer":
        query1 = "SELECT * FROM customer WHERE c_email = %s"
        res1 = db.select(query1, search)
        for res in res1:
            customer_id = res['c_id']
        if customer_id != '':
            query2 = "SELECT * FROM orders NATURAL JOIN customer WHERE c_id = %s"
            ordersFound = db.select(query2, customer_id)
        else:
            return orders

    elif searchType == "order":
        query3 = "SELECT * FROM orders NATURAL JOIN customer WHERE order_id = %s"
        ordersFound = db.select(query3, search)

    for o in ordersFound:
        orders.append({"id": o['order_id'], "c_id": o['c_id'], "email": o['c_email'], "tracking": o['tracking_number'], "transaction":
                       o['transaction_number'], "order_date": o['order_date'], "arrival_date": o['arrival_date'],
                       "ship_date": o['ship_date'], "total_price": o['total_price'], "status": o['order_status']})
    return orders


def getordermodel(ID):
    for key, order in ordersList.items():
        if key == ID:
            return order


def getorderproductsmodel(ID):
    returnList = {}
    num = 1
    for key, product in productsList.items():
        if product['order_id'] == ID:
            if returnList == {}:
                returnList = {'1': product}
            else:
                num += 1
                returnList = MagerDicts(returnList, {str(num): product})
    print(returnList)
    return returnList




