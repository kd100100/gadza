from flask import Flask,render_template,url_for,request,redirect
from mysql.connector import connect
from sign_in import sign_in_database_create_farmer,sign_in_database_create_retailer
from log_in import login_auth_farmer,login_auth_retailer
from farmer_page import get_my_products ,delete_entry, add_entry ,get_avl_requests,sort_and_filter
from retailer_login import get_all_farmer_products,add_entry_retailer,get_my_requests,delete_entry_retailer
from prediction import*
import math

#Appp and database connections
app = Flask(__name__)
con = connect(host='127.0.0.1',user='root',password='',database='gazda')
cursor = con.cursor()


#Index page , Login
@app.route('/',methods=['POST','GET'])
def home():
    if(request.method=='POST'):
        if(request.form['inputGroupSelect01']=="1"):
            if(login_auth_retailer(request,cursor)):
                cursor.execute("""SELECT `Name` FROM `retailers` WHERE PhoneNumber = '{}'""".format(request.form['phone']))
                Name = cursor.fetchall()[0][0] 
                return redirect(url_for('dashboard_retailer',Name=Name.title()))
            else:
                return render_template('index.html',IsWrong="1")
        else:
            if(login_auth_farmer(request,cursor)):
                cursor.execute("""SELECT `Name` FROM `farmers` WHERE PhoneNumber = '{}'""".format(request.form['phone']))
                Name = cursor.fetchall()[0][0] 
                return redirect(url_for('dashboard_farmer',Name=Name.title()))
            else:
                return render_template('index.html',IsWrong="1")
    return render_template('index.html')



#farmer
#signup
@app.route('/signup/farmer',methods=['POST','GET'])
def sign_up_farmer():
    IsUnique = sign_in_database_create_farmer(request,cursor,con)
    if(IsUnique==1):
        return render_template('signup.html',IsUnique=1)  #Successfully registered
    else:
        return render_template('signup.html',IsUnique=2)  #Already in DB

#Signup default page
@app.route('/signup',methods=['POST','GET'])
def sign_up(IsUnique=3):
    if(request.method=='POST'):
        if(request.form['phone_'] == "" or request.form['phone_']== None):
            redirect(url_for('sign_up_farmer'))
        else:
            redirect(url_for('sign_up_retailer'))
    return render_template('signup.html',IsUnique=3) #empty




#Retailer
#signup
@app.route('/signup/retailer',methods=['POST','GET'])
def sign_up_retailer():
    IsUnique = sign_in_database_create_retailer(request,cursor,con)
    if(IsUnique==1):
        return render_template('signup.html',IsUnique=1)  #Successfully registered
    else:
        return render_template('signup.html',IsUnique=2)  #Already in DB



#retailer
#dashborad
@app.route('/retailer/<Name>',methods=['POST','GET'])
def dashboard_retailer(Name):
    if(request.method=='POST'):
        add_entry_retailer(Name,request.form,cursor,con)
    data = get_all_farmer_products(cursor)
    mydata = get_my_requests(Name,cursor)
    return render_template('retailer.html',Name = Name,data = data,mydata=mydata)




#farmer
#dashborad
@app.route('/farmer/<Name>',methods=['POST','GET'])
def dashboard_farmer(Name):
    if(request.method == 'POST'):
        add_entry(Name,request.form,cursor,con)
    data = get_my_products(Name,cursor)
    mydata = get_avl_requests(cursor)
    return render_template('farmer.html',Name = Name,data = data,mydata=mydata)


@app.route('/del/<item>')
def delete_retailer(item):  #Harsh_Tomato_50kg_1000
    delete_entry(item,cursor,con)   
    return redirect(url_for('dashboard_retailer',Name=item.split("_")[0]))




@app.route('/delete/<item>')
def delete(item):  #Harsh_Tomato_50kg_1000
    delete_entry(item,cursor,con)   
    return redirect(url_for('dashboard_farmer',Name=item.split("_")[0]))




@app.route('/WhatsApp/<Name>')
def get_whatsapp(Name):
    cursor.execute(""" SELECT `PhoneNumber` FROM `farmers` WHERE Name = '{}' """.format(Name))
    farmer_no = cursor.fetchall()
    cursor.execute(""" SELECT `PhoneNumber` FROM `retailers` WHERE Name = '{}' """.format(Name))
    retailer_no = cursor.fetchall()
    print(retailer_no,farmer_no)
    if(len(farmer_no)==0):
        link = 'https://wa.me/91' + retailer_no[0][0]
        return redirect(link)
    else:
        link = 'https://wa.me/91' + farmer_no[0][0]
        return redirect(link)




@app.route("/Predictor",methods=['POST','GET'])
def predict_page():
    para_word = extra_rain()
    x = "There will be " + str(round(para_word[0],2)) + " times more rain next month than that of this month."
    sow_crop = findCrop()
    rainfed =  round(get_rain_fed(),2)
    crop_pred_data = (sow_crop,rainfed)
    if(request.method=="POST"):
        x = "The expected rain on " + str(request.form['Year']) + "-" + str(request.form["Month"]) + " is " + str(round(predictRain(int(request.form['Month']),int(request.form['Year']))[0],2)) + "mm"
        return render_template('predictor.html',para_word = x,crop_pred_data = crop_pred_data)
    return render_template('predictor.html',para_word = x,crop_pred_data = crop_pred_data)



if __name__ == "__main__":
    app.run(debug=True)
    con.close()