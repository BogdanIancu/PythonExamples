import matplotlib.pyplot as plt
import pandas
from pandas import Series, DataFrame
import numpy
import matplotlib.pyplot
import seaborn
import patsy
from patsy import dmatrices
import statsmodels.api
from statsmodels.nonparametric.kde import KDEUnivariate


#load the data frame from the .csv file
titanic_df = pandas.read_csv('titanic.csv')
print(titanic_df.head())
#check data statistics
print(titanic_df.info())



# solution from Deep Learning By Example: A hands-on guide to implementing advanced machine learning algorithms and neural networks
# by Ahmed Menshawy

# model formula
# here the ~ sign is an = sign, and the features of our dataset
# are written as a formula to predict survived. The C() lets our 
# regression know that those variables are categorical.
# Ref: http://patsy.readthedocs.org/en/latest/formulas.html

formula = 'Survived ~ C(Pclass) + C(Sex) + Age + SibSp + C(Embarked)' 
results = {}

# create a regression friendly dataframe using patsy's dmatrices function
y,x = patsy.dmatrices(formula, data=titanic_df, return_type='dataframe')

# instantiate our model
model = statsmodels.api.Logit(y,x)

# fit our model to the training data
res = model.fit()

# save the result for outputing predictions later
results['Logit'] = [res, formula]
print(res.summary())


# Plot Predictions Vs Actual
# generate predictions from our fitted model
ypred = res.predict(x)
plt.plot(x.index, ypred, 'bo', x.index, y, 'mo', alpha=.25)
plt.grid(color='white', linestyle='dashed')
plt.title('Logit predictions, Blue: \n Fitted/predicted values: Red')

matplotlib.pyplot.show()

# Residuals
plt.plot(res.resid_dev, 'r-')
plt.grid(color='white', linestyle='dashed')
plt.title('Logit Residuals')

matplotlib.pyplot.show()


kde_res = KDEUnivariate(res.predict())
kde_res.fit()
plt.plot(kde_res.support,kde_res.density)
plt.fill_between(kde_res.support,kde_res.density, alpha=.2)
plt.title("Distribution of our Predictions")

matplotlib.pyplot.show()


plt.scatter(res.predict(),x['C(Sex)[T.male]'] , alpha=.2)
plt.grid(b=True, which='major', axis='x')
plt.xlabel("Predicted chance of survival")
plt.ylabel("Gender Bool")
plt.title("The Change of Survival Probability by Gender (1 = Male)")

matplotlib.pyplot.show()


plt.scatter(res.predict(),x['C(Pclass)[T.3]'] , alpha=.2)
plt.xlabel("Predicted chance of survival")
plt.ylabel("Class Bool")
plt.grid(b=True, which='major', axis='x')
plt.title("The Change of Survival Probability by Lower Class (1 = 3rd Class)")

matplotlib.pyplot.show()


plt.scatter(res.predict(),x.Age , alpha=.2)
plt.grid(True, linewidth=0.15)
plt.title("The Change of Survival Probability by Age")
plt.xlabel("Predicted chance of survival")
plt.ylabel("Age")

matplotlib.pyplot.show()


test_data = pandas.read_csv("test.csv")
# test_data['Survived'] = 1.23
# Use your model to make prediction on our test set. 
# compared_results = model.predict(test_data, results, 'Logit')
# compared_results = Series(compared_results)
# output and submit to kaggle
# compared_results.to_csv("logitregres.csv")