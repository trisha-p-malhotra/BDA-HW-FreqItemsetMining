# coding=utf-8
"""
__desc__ : First run the file "hw4-preprocessing.py"
           This programs runs Apriori and FPGrowth algorithms.

__author__ : "Trisha P Malhotra (tpm6421)"
"""


import time
import csv
from apriori import *
from fp_growth import *
import numpy as np
import matplotlib.pyplot as plt

transaction_file = 'reqd_data.csv'
print(transaction_file.shape())



data_array = np.array(transaction_file)
print("Total number of items in the data set :")
#print np.size(data_array,0)
print len(np.unique(data_array))

minSupportlist = [0.02, 0.05, 0.1, 0.15, 0.2, 0.5]
req_index = minSupportlist.index(0.2)

transactions = []
with open(transaction_file, 'rU') as database:
    for row in csv.reader(database):
        transactions.append(row)


#run Apriori
apriori_min_support = []
run_times_A = []

for minSupport in minSupportlist:
    start_time_A = time.time()
    frequent_items1 = runApriori(transactions, minSupport)
    run_times_A.append(time.time()-start_time_A)

    print("Apriori: Frequent items for min support  :" + str(minSupport*100) + "%")
    print(frequent_items1)
    apriori_min_support.append(frequent_items1)




#run FPgrowth
Fpgrowth_min_support=[]
run_times_FP=[]

for minSupport in minSupportlist:
    start_time_FP =time.time()
    itemsets = find_frequent_itemsets(transactions, minSupport*len(transactions), True)
    frequent_items2 = []
    for itemset, support in itemsets:
        frequent_items2.append((itemset, float(support)/len(transactions)))
        run_times_FP.append(time.time()-start_time_FP)

    print("FPGrowth: Frequent items for min support "+str(minSupport*100)+"%" )
    print(frequent_items2)
    Fpgrowth_min_support.append(frequent_items2)



"""
PLotting Run Times of Apriori and FPGrowth
"""
plt.figure(1)
plt.subplot(121)
plt.plot(minSupportlist,run_times_A,'ro')
plt.title(" Run times of Apriori versus Minimum Support")
plt.xlabel("Minimum support")
plt.ylabel("Time in sec")

plt.subplot(122)
plt.plot(minSupportlist,run_times_FP,'ro')
plt.title("Run times of FPGrowth versus Minimum Support")
plt.xlabel("Minimum Support")
plt.ylabel("Time(seconds)")
plt.show()


"""
Plotting histograms of the length of 
frequent itemsets obtained for minSup = 10
"""
# Apriori
length_10_min_A = []
for sets in apriori_min_support[req_index]:
    length_10_min_A.append(len(sets[0]))

# FPGrowth
length_10_min_FP=[]
for sets in Fpgrowth_min_support[req_index]:
    length_10_min_FP.append(len(sets[0]))

plt.figure()
plt.hist(length_10_min_FP)
plt.title("FPgrowth - Length of frequent item sets - Minimum Support 10 ")
plt.ylabel("Frequency")
plt.show()

plt.figure()
plt.hist(length_10_min_A)
plt.title("Apriori - Length of frequent item sets - Minimum Support 10 ")
plt.ylabel("Frequency")
plt.show()



"""
Q. 
For minSup=10%, choose 5 frequent itemsets that contains “<=50K” (choose itemsets with more than3 items). 
Consider the rule  X ->“<50 K”, where X are the  other items in your frequent itemset. 
Find the confidence of your rule for each of the frequent itemsets you chose
"""
items5_less_50k_min10_apr = []
count = 0
for sets in apriori_min_support[req_index]:

    if " <=50K" in sets[0] and len(sets[0]) > 3:
        items5_less_50k_min10_apr.append(sets[0])
        count += 1
        if count == 5:
            break


items5_less_50k_min10_FPg = []
count = 0
for sets in Fpgrowth_min_support[req_index]:
    if " <=50K" in sets[0] and len(sets[0]) > 3:
        items5_less_50k_min10_FPg.append(sets[0])
        count += 1
        if count == 5:
            break

"""
For 5 frequent itemsets that contains “>50"
"""
items5_greater_50k_min10_apr = []
count = 0
for sets in apriori_min_support[req_index]:

    if " >50K" in sets[0] and len(sets[0]) > 3:
        items5_greater_50k_min10_apr.append(sets[0])
        count += 1
        if count == 5:
            break

items5_greater_50k_min10_FPg = []
count=0
for sets in Fpgrowth_min_support[req_index]:
    if " >50K" in sets[0] and len(sets[0]) > 3:
        items5_greater_50k_min10_FPg.append(sets[0])
        count += 1
        if count == 5:
            break

print("================================================")
print(" 5 frequent item sets that contains <=50K  and set length > 3 with min support 10 FPgrowth")
print(items5_less_50k_min10_FPg)
print(" 5 frequent item sets that contains <=50K  and set length > 3 with min support 10 Apriori")
print(items5_less_50k_min10_apr)
print(" 5 frequent item sets that contains >50K  and set length > 3 with min support 10 FPgrowth")
print(items5_greater_50k_min10_FPg)
print(" 5 frequent item sets that contains >50K  and set length > 3 with min support 10 Apriori")
print(items5_greater_50k_min10_apr)