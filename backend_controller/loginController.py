from backend_model.loginModel import *
from flask import session, redirect


def logincontroller(email, password):
    result = loginmodel(email=email, password=password)

    if result == "true":
        # If entering from another page
        if 'request' in session:
            request = session['request']
            session.pop('request', None)
            return redirect(request)
        else:
        # If entering from regular login page
            return redirect("/products")
    else:
        # Could not lot in successfully
        return redirect("/message")

