import pandas as pd
from sklearn import linear_model
import pickle

data = pd.read_csv('data_new.csv')
data.head(11)
crop_sow = {'Year': list(data["Year"]),
            'Month': list(data["Month"]),
            'Rainfall': list(data["Rainfall"])
            }

df = pd.DataFrame(crop_sow,columns=['Year','Month','Rainfall'])

X = df[['Year','Month']]
Y = df['Rainfall']
 
# with sklearn
regr = linear_model.LinearRegression()
regr.fit(X, Y)

print('Intercept: \n', regr.intercept_)
print('Coefficients: \n', regr.coef_)
pickle.dump(regr, open('model.pkl','wb'))





