def login_auth_farmer(request,cursor):
    cursor.execute(""" SELECT `Password` FROM `farmers` WHERE PhoneNumber = '{}'""".format(request.form['phone']))
    password = cursor.fetchall()
    if(len(password)>0):
        if(password[0][0]==request.form['pwd']):
            return True
        else:
            return False
    else:
        return False

def login_auth_retailer(request,cursor):
    cursor.execute(""" SELECT `Password` FROM `retailers` WHERE PhoneNumber = '{}'""".format(request.form['phone']))
    password = cursor.fetchall()
    if(len(password)>0):
        if(password[0][0]==request.form['pwd']):
            return True
        else:
            return False
    else:
        return False