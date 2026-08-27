import csv
import os
name= input("Enter student name:")
subjects=["python","java","c++", "Database"]
marks=[]
for subject in subjects:
    mark= float(input(f"Enter marks for {subject}: "))
    marks.append(mark)
total= sum(marks)
average= total/len(subjects)
if average >= 90:
    grade= "A+"
elif average >= 80:
    grade= "A"
elif average >= 70:
    grade= "B"
elif average >= 60:
    grade= "B+"
elif average >= 50:
    grade= "D"
else:
    grade= "F"

result = "PASS" if average >= 40 else "FAIL"

print(f"\nStudent Name: {name}")
print(f"Total Marks: {total}")
print(f"Average Marks: {average:.2f}")
print(f"Grade: {grade}")
print(f"Result: {result}")

file_name= "student_results.csv"
file_exists= os.path.exists(file_name)

with open(file_name, mode='a', newline='') as file:
    writer= csv.writer(file)
    if not file_exists:
        writer.writerow(["Name","Total Marks", "Average","Grade", "Results"])
    writer.writerow([name,total,round(average, 2), grade,result])
print(f"\nResults saved to {file_name}")  