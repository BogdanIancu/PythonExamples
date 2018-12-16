import pandas

data = pandas.read_csv('C:\\Users\\bogda\\Desktop\\Python\\PythonExamples\\day_6\\sample_files\\mydata.csv')
print(data)
dataH = pandas.read_csv('C:\\Users\\bogda\\Desktop\\Python\\PythonExamples\\day_6\\sample_files\\mydata.csv', header=None)
print(dataH)

print('------- Excel values --------')
document = pandas.ExcelFile('C:\\Users\\bogda\\Desktop\\Python\\PythonExamples\\day_6\\sample_files\\mydata.xlsx')
data = document.parse('Sheet1')
print(data)