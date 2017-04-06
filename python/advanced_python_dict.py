#Q6:

import csv
import re

filename = 'faculty.csv'

faculty_dict = {}

def new_faculty_dict():
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

for key, value in sorted(new_faculty_dict().items())[:3]:
	print (key, value)
#I tried using itertools/islice here but I couldn't get it to work properly.

#Q7: 

import csv
import re

filename = 'faculty.csv'
    
def new_professor_dict():
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

for key, value in sorted(new_professor_dict().items())[:3]:
	print (key, value)
    
#Q8:

import csv
import re

filename = 'faculty.csv'
    
def new_professor_dict():
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

for key, value in sorted(new_prof().items(), key = lambda k: k[0][1])[:3]:
	print (key, value)
