import csv

with open('AdventOfCodeData-1.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter='\n')
    numbers = []
    for row in reader:
        numbers.append(int(row[0]))

print(numbers)

# Brute Force
for numberone in numbers:
    for numbertwo in numbers:
        for numberthree in numbers:
            if (numberone + numbertwo + numberthree == 2020):
                print(numberone * numbertwo * numberthree)

# Binary Tree
