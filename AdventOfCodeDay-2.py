import csv

with open('AdventOfCodeData-2.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter='\n')
    data = []
    for row in reader:
        # figure out how to parse the lower and upper bounds from the data
        data.append(int(row[0]))

print(data)
