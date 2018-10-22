
import csv

count = 0
data_array = []
data_array.append(['Age','Sex','CP','Trestbps','chol','FBS','ResteCG','Thalach','Exang','Oldpeak','Slope','CA','Thal','Num'])

with open("/home/antu/dataset.data") as file:
     for line in file:
         row = line.strip().split(' ')
         data_array.append(row)

if (count != 0):
    for i in range(1,len(data_array)):
        row = data_array[i]
        for j in range(len(row)):
            row[i] = float(row[i])

count = count + 1
data_array.remove(data_array[len(data_array)-1])
print(data_array)
datasetFile = open('/home/antu/DataSet/HeartDiseaseDataset.csv','w')

with datasetFile:
    writer = csv.writer(datasetFile)
    writer.writerows(data_array)

print("Writing Complete")
