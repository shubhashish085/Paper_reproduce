import pandas
import csv

health_data = pandas.read_csv("/home/antu/DataSet/HeartDiseaseDataset.csv")

ratio_array = [5,1,1,20,50,1,1,20,1,1,1,2,2,1]

column_headers = list(health_data)

main_array = []

main_array.append(column_headers)

for i in range(1,len(health_data)):
    array = []
    for j in range(len(ratio_array)):
        print(health_data[column_headers[j]][i]/ratio_array[j])
        array.append(int(round(health_data[column_headers[j]][i]/ratio_array[j],0)))
    main_array.append(array)


myFile = open('/home/antu/DataSet/DiscretizedData.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(main_array)

print('Writing Complete')


