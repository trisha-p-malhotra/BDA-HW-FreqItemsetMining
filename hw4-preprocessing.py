"""
__desc__ : "Converts Continuous columns into Categories"
__author__ : "Trisha P Malhotra (tpm6421)"
"""

import numpy as np
import pandas as pd


adult_data_input = pd.read_csv("adult.data")
data_matrix = np.matrix(adult_data_input)
"""
Preprocessing
"""
# Getting matrix columns of the 4 continuous columns
age = data_matrix[:,[0]]

capital_gain = data_matrix[:,[10]]

capital_loss = data_matrix[:,[11]]

hours_per_week =data_matrix[:,[12]]


# Update Age
for i in range(0,len(age)):
    value = age[i]
    if(value <= 19):
        value = "teens"
    elif(value <= 29):
        value = "twenties"
    elif (value <= 39):
        value = "thirties"
    elif (value <= 49):
        value = "forties"
    elif (value <= 59):
        value = "fifties"
    elif(value <= 69):
        value = "sixties"
    elif (value <= 79):
        value = "seventies"
    elif (value <= 89):
        value = "eighties"
    elif (value <= 99):
        value = "ninties"
    else:
        value = "oldest"
    age[i] = value


# Update Capital gain
for i in range(0,len(capital_gain)):
    value = capital_gain[i]
    if value <= 5000:
        value = "<5000"
    elif value <= 10000:
        value = "5000-10000"
    elif value <= 20000:
        value = "10000-20000"
    elif value <= 10000:
        value = "20000-30000"
    else:
        value = ">30000"
    capital_gain[i] = value


# Update Capital Loss
for i in range(0,len(capital_loss)):
    value = capital_loss[i]
    if value <= 200:
        value ="0_200"
    elif value <= 500:
        value = "200_500"
    elif value <= 1000:
        value = "500_1000"
    elif value <= 2000:
        value = "1000_2000"
    elif value <= 3000:
        value = "2000_3000"
    else:
        value = "<3000"
    capital_loss[i] = value


# Update Hours per Week
for i in range(0,len(hours_per_week)):
    value = hours_per_week[i]
    if(value <= 19):
        value = "10_19"
    elif(value <= 29):
        value = "20_29"
    elif (value <= 39):
        value = "30_39"
    elif (value <= 49):
        value = "40_49"
    elif (value <= 59):
        value = "50_59"
    elif(value <= 69):
        value = "60_69"
    elif (value <= 79):
        value = "70_79"
    elif (value <= 89):
        value = "80_89"
    elif (value <= 99):
        value ="90_99"
    else:
        value = "100plus"
    hours_per_week[i] = value


# Modify original dataset as per required data set:
data_matrix[:, 0] = age
data_matrix[:, 10] = capital_gain
data_matrix[0:, 11] = capital_loss
data_matrix[:, 12] = hours_per_week

# Not including columns :: fnlwgt and Education Num
updated_data_set = data_matrix[:, [0, 1, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]]

filedata = pd.DataFrame(updated_data_set)

filedata.to_csv("reqd_data.csv", header=None, index=None)



