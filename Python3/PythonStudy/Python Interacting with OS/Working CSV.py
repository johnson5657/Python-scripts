import csv
f = open("2222.txt")
csvfile = csv.reader(f) #using the csv reader will read the CSV file and parse it each line in the file is a list of value
for line in csvfile:
    for i in line:
        print(i)#this will print each item in each line of the CSV file


#########################
#GENERATEING CS FILE
#########################


hosts= [["fdsfdsf","1.1.1.1"],["fdsfdsfds3333","2.2.2.2"],["32321312321d","3.3.3.3"]]

with open("hosts.csv","w") as f:
    writercsv =  csv.writer(f) # creating a csv.writer object and associate ti with a file
    writercsv.writerows(hosts)  # write our list hosts to the file in csv format


#############################
# Read and write CSV filw with Dictionary

with open("hosts.csv") as f:
    ReaderDict  = csv.DictReader(f)
    for row in ReaderDict:
        print(row)