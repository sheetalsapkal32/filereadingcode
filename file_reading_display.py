
with open('./testfile.csv', 'r') as csv: #open the csv file 
     first_line = csv.readline()   #read lines 
     data = csv.readlines()
tot_col = first_line.count(',') + 1
print(tot_col)
print (data)
