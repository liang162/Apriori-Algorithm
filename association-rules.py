import sys
import csv
import math
import random
import numpy as np
from itertools import combinations

dataFilename = sys.argv[1]
support = sys.argv[2]
confidence = sys.argv[3]

#data[1] = ['0: 1', '1: Paradise Valley', '2: AZ', '3: 4', '4: full_bar', '5: quiet', '6: dressy', '7: 3', '8: FALSE', '9: TRUE', '10: FALSE']
#len(data) = 9338, the first row is useless
data = []

#result[7] = [3, 1, 1, 2, 2, ...]
result = []

with open(dataFilename) as csvfile:
    temp_data = csv.reader(csvfile, delimiter=',')
    for row in temp_data:
        data.append(row)

for i in range(0, len(data)):
    for j in range(0, len(data[0])):
        data[i][j] = str(j) + ": " + data[i][j]

#transpose
temp = []
for i in range(0, len(data[1])):
    for j in range(1, len(data)):
        temp.append(data[j][i])
    result.append(temp)
    temp = []

#find total unique value
total_unique = []
single = []
for i in range(0, 11):
    total_unique.append(len(np.unique(result[i])))
    for j in range(0, len(np.unique(result[i]))):
        if(i == 0):
            single.append(np.unique(result[i])[j])
        elif(i == 1):
            single.append(np.unique(result[i])[j])
        elif(i == 2):
            single.append(np.unique(result[i])[j])
        elif(i == 3):
            single.append(np.unique(result[i])[j])
        elif(i == 4):
            single.append(np.unique(result[i])[j])
        elif(i == 5):
            single.append(np.unique(result[i])[j])
        elif(i == 6):
            single.append(np.unique(result[i])[j])
        elif(i == 7):
            single.append(np.unique(result[i])[j])
        elif(i == 8):
            if(np.unique(result[i])[j] == "TRUE"):
                single.append(np.unique(result[i])[j])
        elif(i == 9):
            if(np.unique(result[i])[j] == "TRUE"):
                single.append(np.unique(result[i])[j])
        elif(i == 10):
            if(np.unique(result[i])[j] == "TRUE"):
                single.append(np.unique(result[i])[j])

# start
# frequent single items
minsup = (len(data) - 1) * float(support)
mincon = (len(data) - 1) * float(confidence)

# frequent itemsets
while(True):
    count = 0
    if(count == 0):
        break

association_rule_dict = {}
association_rule_table = []

Cn = list(combinations(single, 1))
Ln = []
for tuple_Cn in Cn: # ('0: 1', '0: 0')
    count = 0
    for csv_row in data: #['0: 1', '1: Paradise Valley', '2: AZ']
        flag = 1
        for element in tuple_Cn: #'0: 1'
            if(csv_row.count(element) == 0):
                flag = 0
        if(flag == 1):
            count = count + 1
    if(count > minsup):
        Ln.append(tuple_Cn[0])
        association_rule_dict[tuple_Cn] = count

for i in range(2, 100):
    Rn = []
    LL = list(combinations(Ln, i))
    for tuple_Ln in LL: # ('0: 1', '0: 0')
        count = 0
        for csv_row in data: #['0: 1', '1: Paradise Valley', '2: AZ']
            flag = 1
            for element in tuple_Ln: #'0: 1'
                if(csv_row.count(element) == 0):
                    flag = 0
            if(flag == 1):
                count = count + 1
        if(count > minsup):
            Rn.append(tuple_Ln)
            association_rule_dict[tuple_Ln] = count
    if(len(Rn) == 0):
        break
    else:
        print "FREQUENT-ITEMS" + " " + str(i) + " " + str(len(Rn))
        association_rule_table.append(Rn)

# association rule
print association_rule_table
print association_rule_dict







