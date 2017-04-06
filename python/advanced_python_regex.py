#Q1:

import re
import csv
import string

filename = 'faculty.csv'

with open(filename) as csv_file:
    next(csv_file, None)
    faculty_csv = csv.reader(csv_file, delimiter=',')
    counts = dict()
    for row in faculty_csv:
        output = row[1]
        if len(output) > 1:
            degree = str(output)
            degree = degree.translate(str.maketrans("", "", string.punctuation))
            words = degree.split()
            for word in words:
                if word not in counts: 
                    counts[word] = 1
                else:
                    counts[word] += 1       
print(counts)
print(len(counts))

#Q2:

import re
import csv
import string

filename = 'faculty.csv'

with open(filename) as csv_file:
    next(csv_file, None)
    faculty_csv = csv.reader(csv_file, delimiter=',')
    counts = dict()
    for row in faculty_csv:
        output = row[2]
        if len(output) > 1:
            line = str(output)
            line = line.strip()
            x = re.split("(Professor)+", line)
            del x[-1]
            y = ' '.join(x)
            if y not in counts: 
                counts[y] = 1
            else:
                counts[y] += 1

print(counts)
print(len(counts))

#Q3:

import re
import csv
import string

filename = 'faculty.csv'

with open('faculty.csv') as csv_file:
    next(csv_file, None)
    faculty_csv = csv.reader(csv_file, delimiter=',')
    emails = list()
    for row in faculty_csv:
        output = row[3]
        if len(output) > 1:
            x = str(output)
            emails.append(x)

for x in emails:
    print(x)
    
#Q4:

import re
import csv
import string

with open('faculty.csv') as csv_file:
    next(csv_file, None)
    faculty_csv = csv.reader(csv_file, delimiter=',')
    domains = dict()
    for row in faculty_csv:
        output = row[3]
        if len(output) > 1:
            line = str(output)
            line = line.strip()
            x = re.split("(@)+", line)
            y = x[-1]
            if y not in domains: 
                domains[y] = 1
            else:
                domains[y] += 1

print(domains)
print(len(domains))    
