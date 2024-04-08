from backend_model.connectDB import *
product0List = [['1', "Tello Drone", 'DJI', 'desc here', 'Yes', '480p', 'White', 'dji_tello.jpg', '15', 'active', '89.00', '89.00'],
               ['2', 'Bebop 2', 'Parrot', 'desc', 'Yes', '1080p', 'Red', 'parrot_bebop_2.jpg', '3', 'active', '270.00', '290.00'],
               ['3', 'Bebop 2', 'Parrot', 'desc', 'Yes', '1080p', 'Red', 'parrot_bebop_2.jpg', '3', 'active', '270.00', '290.00']]




def getProductsModel():
    db = Dbconnect()
    productList = []

    query = "SELECT * FROM products"
    productsFound = db.select(query)

    for p in productsFound:
        productList.append({"id": p['p_id'], "name": p['p_name'], "brand": p['p_brand'], "desc": p['p_desc'],
                            "wifi": p['p_wifi'], "video_res": p['p_video_res'], "color": p['color'],
                            "img": p['p_img'], "stock": p['stock'], "cost": p['p_cost'], "price": p['p_price'],
                            "status": p['p_status']})
    return productList


# Find the specific product given the ID, found in element 0 of the sub-arrays
def getsingleproductmodel(prodID):
    for product in product0List:
        if product[0] == prodID:
            return product


def createNewProductModel(name, brand, video_res, wifi, color, price, cost, stock, img, status):
    # DB credentials found in backend_model/connectDB.py
    db = Dbconnect()
    query = "INSERT INTO products(p_name, p_brand, p_video_res, p_wifi, color, p_price, p_cost," \
            "stock, p_img, p_status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    db.execute(query, (name, brand, video_res, wifi, color, price, cost, stock, img, status))
    return

