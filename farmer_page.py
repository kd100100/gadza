import datetime

def get_my_products(Name,cursor):
    cursor.execute("""SELECT * FROM `{}` WHERE IsAvaliable='1'""".format(Name))
    data = cursor.fetchall() #[('Tomato', '1', '2020-09-30', '50kg', 'Alandur', '1000', 'Farmer', '1')]
    return data


def get_avl_requests(cursor):
    cursor.execute("""SELECT `Name` FROM `retailers`""")
    dummy = cursor.fetchall()  #[('Manoah'),('harsh')]
    data = []  #[('Tomato', '1', '2020-09-30', '50kg', 'Alandur', '1000', 'Farmer'), ('Brinjal', '0', '2020-10-10', '13', 'Alandur', '2345', 'Retailer')]
    for i in dummy:
        cursor.execute(""" SELECT `GoodsName`, `IsOrganic`, `DatePosted`, `Quantity`, `Region`, `OfferedPrice`, `Shipping` FROM `{}`
        """.format(i[0]))
        data = data+cursor.fetchall()
    return data

def delete_entry(item,cursor,con):
    item_l = item.split("_") #Harsh_Tomato_50kg_1000
    #data = get_my_products(item_l[0],cursor)
    cursor.execute("""DELETE FROM `{}` WHERE GoodsName = '{}' and Quantity = '{}' and OfferedPrice = '{}'
    """.format(item_l[0],item_l[1],item_l[2],item_l[3]))
    con.commit()


#INSERT INTO `harsh`(`GoodsName`, `IsOrganic`, `DatePosted`, `Quantity`, `Region`, `OfferedPrice`, `Shipping`, `IsAvaliable`)
#  VALUES ("Tomato","1","2020-09-30","50kg","Alandur","1000","Farmer","1")
def add_entry(Name,data,cursor,con):
    if(data['IsOrganic']=="1"):
        isOrganic = 1
    else:
        isOrganic = 0

    x = datetime.datetime.now()
    datE = str(x).split()[0]

    if(data['ShippingType']=="0"):
        sHip = "Farmer"
    else:
        sHip = "Retailer"

    cursor.execute("""INSERT INTO `{}` (`GoodsName`, `IsOrganic`, `DatePosted`, `Quantity`, `Region`, `OfferedPrice`, `Shipping`, `IsAvaliable`) VALUES ('{}','{}','{}','{}','{}','{}','{}','1')""".format(Name,data['product'],isOrganic,datE,data['Quantity'],data['Region'],data['Price'],sHip))
    
    con.commit()



def sort_and_filter(mydata):
    dummy_list = mydata.copy()
    mydata.clear()
    for i in dummy_list:
        if(i[1]=="1"):
            mydata.append(i)
    return mydata