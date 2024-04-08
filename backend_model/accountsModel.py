from backend_model.connectDB import *


# Get all accounts
def getaccountsmodel(userType):
    # DB credentials found in backend_model/connectDB.py
    db = Dbconnect()
    usersList = []

    if userType == 'administrator':
        query = "SELECT * from admin"
        adminFound = db.select(query)

        for user in adminFound:
            usersList.append(
                {"id": user['admin_id'], "first_name": user['a_firstname'], "last_name": user['a_lastname'],
                 "email": user['a_email'], "phone_number": user['a_phone_number'],
                 "status": user['a_status']})
    elif userType == 'customer':
        query = "SELECT * from customer"
        customerFound = db.select(query)

        for user in customerFound:
            usersList.append(
                {"id": user['c_id'], "first_name": user['c_first_name'], "last_name": user['c_last_name'],
                 "email": user['c_email'], "phone_number": user['c_phone_number'],
                 "status": user['c_status']})
    return usersList

# Get the specific account requested
# In this case, we're requesting it via the key
def getaccountmodel(acc, userType):
        db = Dbconnect()
        usersList = []
        if userType == 'customer':
            table = 'customer'
            table_id = 'c_id'
        elif userType == 'administrator':
            table = 'admin'
            table_id = 'admin_id'

        query = f"SELECT * FROM {table} WHERE {table_id} = %s"
        userFound = db.select(query, (acc, ))

        for user in userFound:
            if userType == 'customer':
                usersList.append(
                {"id": user['c_id'], "first_name": user['c_first_name'], "last_name": user['c_last_name'],
                 "email": user['c_email'],
                 "phone_number": user['c_phone_number'], "status": user['c_status']})
            elif userType == 'administrator':
                usersList.append(
                    {"id": user['admin_id'], "first_name": user['a_firstname'], "last_name": user['a_lastname'],
                     "email": user['a_email'], "phone_number": user['a_phone_number'],
                     "status": user['a_status']})
        return usersList

def updateAccountModel(uinfo, userType, id):
    db = Dbconnect()
    if userType == 'administrator':
        table = 'admin'
        table_id = 'admin_id'
        table_fname = 'a_firstname'
        table_lname = 'a_lastname'
        table_num = 'a_phone_number'
        table_status = 'a_status'
    elif userType == 'customer':
        table = 'customer'
        table_id = 'c_id'
        table_fname = 'c_first_name'
        table_lname = 'c_last_name'
        table_num = 'c_phone_number'
        table_status = 'c_status'

    query = (
        f"UPDATE {table} "
        f"SET {table_fname} = %s, {table_lname} = %s, {table_num} = %s, {table_status} = %s "
        f"WHERE {table_id} = %s"
    )

    print("STATUS IN MODEL: ", uinfo['status'])

    db.execute(query, (uinfo['fname'], uinfo['lname'], uinfo['phone_num'], uinfo['status'], id))

    print("QUERY: ", query)

    return



