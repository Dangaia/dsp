import csv

emails = []
f = open('faculty.csv')
faculty_csv = csv.reader(f)

next(faculty_csv)
for row in faculty_csv:
    emails.append(row[3])  
with open("emails.csv", "w") as f:
    write_faculty_csv = csv.writer(f)
    for email in emails:
        write_faculty_csv.writerow([email])
