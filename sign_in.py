def sign_in_database_create_farmer(request,cursor,con):
        cursor.execute(""" SELECT `PhoneNumber` FROM `farmers` """)
        phone_numbers = cursor.fetchall()
        IsUnique = 1
        #print(phone_numbers)  [('8610342197',), ('9176580040',)]
        #check if phone number matches
        for i in phone_numbers:
            if(i[0]==request.form['phone']):
                IsUnique = 2

        if(IsUnique==1):
            cursor.execute(""" INSERT INTO `farmers`(`Name`, `PhoneNumber`, `Password`) VALUES ( '{}','{}','{}')"""
            .format(request.form['fname'],request.form['phone'],request.form['pwd']))
            con.commit()

            cursor.execute(""" CREATE TABLE `{}` ( `GoodsName` VARCHAR(100) NOT NULL ,
             `IsOrganic` VARCHAR(10) NOT NULL , `DatePosted` VARCHAR(10) NOT NULL , `Quantity` VARCHAR(10) NOT NULL ,
              `Region` VARCHAR(100) NOT NULL , `OfferedPrice` VARCHAR(100) NOT NULL ,
               `Shipping` VARCHAR(100) NOT NULL , `IsAvaliable` VARCHAR(10) NOT NULL )""".format(request.form['fname']))
            con.commit()
        return IsUnique   #1 success 2failed 3empty 
    



#retailer
def sign_in_database_create_retailer(request,cursor,con):
        cursor.execute(""" SELECT `PhoneNumber` FROM `retailers` """)
        phone_numbers = cursor.fetchall()
        IsUnique = 1
        #print(phone_numbers)  [('8610342197',), ('9176580040',)]
        #check if phone number matches
        for i in phone_numbers:
            if(i[0]==request.form['phone_']):
                IsUnique = 2

        if(IsUnique==1):
            cursor.execute(""" INSERT INTO `retailers`(`Name`, `PhoneNumber`, `Password`) VALUES ( '{}','{}','{}')"""
            .format(request.form['fname'],request.form['phone_'],request.form['pwd']))
            con.commit()

            cursor.execute(""" CREATE TABLE `{}` ( `GoodsName` VARCHAR(100) NOT NULL ,
             `IsOrganic` VARCHAR(10) NOT NULL , `DatePosted` VARCHAR(10) NOT NULL , `Quantity` VARCHAR(10) NOT NULL ,
              `Region` VARCHAR(100) NOT NULL , `OfferedPrice` VARCHAR(100) NOT NULL ,
               `Shipping` VARCHAR(100) NOT NULL , `IsAvaliable` VARCHAR(10) NOT NULL )""".format(request.form['fname']))
            con.commit()
        return IsUnique   #1 success 2failed 3empty 