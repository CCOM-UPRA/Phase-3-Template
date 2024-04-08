from flask import session
from backend_model.connectDB import *
import pymysql
from passlib.hash import sha256_crypt


def loginmodel(email, password):
    # DB credentials found in backend_model/connectDB.py
    db = Dbconnect()
    admin = []

    query = "SELECT * from admin WHERE a_email = %s"
    adminFound = db.select(query, email)

    for user in adminFound:
        session['admin'] = user['admin_id']
        admin.append({"id": user['admin_id'], "email": user['a_email'], "password": user['a_password'],
                      "status": user['a_status']})

    if not admin:
        print("NO ADMIN FOUND")
        return "false"
    else:
        for u in admin:
            if email == u['email'] and sha256_crypt.verify(password, u['password']) is True:
                if u['status'] == 'active':
                    print("ACTIVE ADMIN FOUND")
                    session['admin'] = u['id']
                    # Create the session['admin'] saving the admin ID if user is found
                    return "true"
                else:
                    print("INCORRECT ADMIN STATUS")
            else:
                print("INCORRECT ADMIN CREDENTIALS")
                # If it didn't find this active admin account
                return "false"



