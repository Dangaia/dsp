import csv
import string
import re

with open('faculty.csv') as csv_file:
    next(csv_file, None)
    faculty_csv = csv.reader(csv_file, delimiter=',')
    counts = dict()
    for row in faculty_csv:
        row1 = row[0]
        degree = row[1]
        degree = degree.strip()
        title = row[2]
        line = title.strip()
        line = str(line)
        x = re.split("(Professor)+", line)
        x = list(filter(None, x))
        del x[-1]
        y = ' '.join(x)
        email = row[3]
        words = row1.split()
        last_name = words[-1]
        desc = list()
        desc.append(degree)
        desc.append(y)
        desc.append(email)
        if last_name not in counts: 
            counts[last_name] = list()
            counts[last_name].append(desc)
        else:
            counts[last_name].append(desc)
                    
print(counts)
