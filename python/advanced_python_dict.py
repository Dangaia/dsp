#Q6:

import csv
import re

filename = 'faculty.csv'

def make_faculty_dict():
	faculty_dict = {}
	with open(filename, 'r') as f:
		faculty_csv = csv.reader(f, delimiter=',')
		next(faculty_csv)

		for row in faculty_csv:
			names = row[0]
			degrees = row[1].strip()
			titles = row[2]
			emails = row[3]

			last_name = re.findall(r'[A-Z][a-z]*\S$', names)

			for item in last_name:
				if item not in faculty_dict:
					faculty_dict[item] = [degrees, titles, emails]
				else:
					faculty_dict[item] = [[degrees, titles, emails], faculty_dict[item]]

	return faculty_dict

print (make_faculty_dict())

#Q7: 

import csv
import re

filename = 'faculty.csv'
    
def make_professor_dict():
	professor_dict = {}
	with open(filename, 'r') as f:
		faculty_csv = csv.reader(f, delimiter=',')
		next(faculty_csv)

		for row in faculty_csv:
			names = row[0]
			degrees = row[1].strip()
			titles = row[2]
			emails = row[3]

			last_name = re.findall(r'[A-Z][a-z]*\S$', names)
			first_name = re.findall(r'^[A-Z][a-z]*\S*', names)

			name = zip(first_name, last_name)

			for item in name:
				professor_dict[item] = [degrees, titles, emails]

	return professor_dict

for k, v in sorted(make_professor_dict().items())[:3]:
	print (k, v)
    
#Q8:
for k, v in sorted(make_prof().items(), key = lambda k: k[0][1])[:3]:
	print (k, v)
