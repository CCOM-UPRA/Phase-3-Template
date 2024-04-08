from backend_model.reportsModel import *


def getReport(timeframe, start_date, end_date, product):
    if timeframe == 'Day':
        query = "SELECT * FROM orders JOIN contains JOIN products WHERE orders.order_id = contains.order_id AND " \
                "contains.p_id = products.p_id AND order_date = %s AND p_name = %s"
    else:
        query = "SELECT *" \
                "FROM orders JOIN contains JOIN products WHERE orders.order_id = contains.order_id AND contains.p_id = products.p_id " \
                "AND order_date BETWEEN %s AND %s AND p_name = %s"
    return getReportModel(timeframe, query, start_date, end_date, product)

def getDatedReport():
    return getDatedReportModel()


def getStockReport():
    return getStockReportModel()
