import pickle
import datetime

def predictRain(Month,Year):
    regr = pickle.load(open('model.pkl','rb'))
    output = regr.predict([[Year,Month]])
    return output


def extra_rain():
    x = datetime.datetime.now()
    curr_mon = float(x.strftime("%m"))

    if(curr_mon==12):
        next_mon = 1
    else:
        next_mon = curr_mon + 1

    y = datetime.datetime.now()
    curr_year = float(y.strftime("%Y"))
    #next_year = curr_mon + 1

    return predictRain(curr_mon,curr_year)/predictRain(next_mon,curr_year)


def findCrop():
    x = datetime.datetime.now()
    curr_mon = float(x.strftime("%m"))

    if(curr_mon==12):
        next_mon = 1
    else:
        next_mon = curr_mon + 1

    y = datetime.datetime.now()
    curr_year = float(y.strftime("%Y"))
    #next_year = curr_mon + 1

    rain =  predictRain(next_mon,curr_year)[0]

    if(500<=rain<=800):
        return "Maize"
    elif(400<=rain<=450):
        return "Finger Millet"
    elif(500<=rain<=700):
        return "Groundnut"
    elif(450<=rain<=650):
        return "Sorghum"
    elif(500<=rain<=700):
        return "Chilli"
    elif(rain>=1500):
        return "Sugar Cane"
    else:
        return "Rice"


def get_rain_fed():
    x = datetime.datetime.now()
    curr_mon = float(x.strftime("%m"))

    if(curr_mon==12):
        next_mon = 1
    else:
        next_mon = curr_mon + 1

    y = datetime.datetime.now()
    curr_year = float(y.strftime("%Y"))
    #next_year = curr_mon + 1

    rain =  predictRain(next_mon,curr_year)[0]

    return rain