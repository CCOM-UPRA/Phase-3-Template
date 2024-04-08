from backend_model.productsModel import *


def getProducts():
    return getProductsModel()


def getsingleproduct(prodID):
    return getsingleproductmodel(prodID)


def createNewProduct(name, brand, video_res, wifi, color, price, cost, stock, img, status):
    price = float(price)
    cost = float(cost)
    stock = int(stock)

    return createNewProductModel(name, brand, video_res, wifi, color, price, cost, stock, img, status)
