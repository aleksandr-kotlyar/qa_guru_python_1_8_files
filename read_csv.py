import csv

f = csv.DictReader('resources/username.csv', 'r')
print(f.reader)