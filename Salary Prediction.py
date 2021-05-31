import pandas
import numpy
ds = pandas.read_csv('Salary_Data.csv')
X = ds['YearsExperience'].values.reshape(30,1)
Y = ds['Salary']
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X,Y)
exp = int(input("\n Enter candidate's experience in years :"))
salary = model.predict([[exp]])
print("\n The salary of candidate is ",salary)
coef = model.coef_
print("\n The value of coefficient is ",coef)
import joblib
joblib.dump(model,'salary.pk1')
print("\n Saved the trained model!")