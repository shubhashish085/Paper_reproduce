import pandas as pd
import csv
import numpy
import math


dataset = pd.read_csv('/home/antu/DataSet/DiscretizedData.csv')

column_headers = list(dataset)

selected_columns = []


def get_entropy(attribute,array):
    feature_list = numpy.zeros(shape=(len(array),5))
    target_attribute_list = dataset[column_headers[13]]
    count_list = numpy.zeros(shape=(len(array)))


    for i in range(1,len(dataset)):
        row_index = array.index(dataset[attribute][i])
        feature_list[row_index][target_attribute_list[i]] = feature_list[row_index][target_attribute_list[i]] + 1
        count_list[row_index] = count_list[row_index] + 1

    return feature_list, count_list


set_array = []

for i in range(len(column_headers)):
    set_array.append(set(dataset[column_headers[i]]))


for i in range(len(set_array[13])):
    for j in range(len(column_headers) - 1):
        array = list(set_array[j])
        entropy_array,count_array = get_entropy(column_headers[j],array)
        for k in range(len(array)):
            if(count_array[k] > 10):
                entropy = 0
                for l in range(5):
                    p_i = (entropy_array[k][l]/count_array[k])
                    if (p_i != 0):
                        entropy = entropy + ((-1) * p_i * math.log(p_i, 2.0))
                if(entropy < 1):
                    selected_columns.append(column_headers[j])
                    break


selected_columns = set(selected_columns)

print(selected_columns)






