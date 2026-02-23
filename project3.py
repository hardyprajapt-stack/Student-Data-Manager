# student data manager
name = input("student name: ")
age = int(input("student age: "))
grade = input("enter grade (A/B/C/D): ")
subject = input("enter subject (hindi,english,science,maths): ").split(",")



# tuple for immutable info
student_id = input("enter student id: ")
dob = input("enter student date of birth : ")
identity = (student_id, dob)



# set for unique subjects
unique_subjects = set(subject)
print("unique_subjects:" ,unique_subjects)


# Dictionary for student record
student_record = {
    "name" : name,
    "age" : age,
    "grade" : grade,
    "subject" : subject
}
#list to store multiple students
students = []
students.append((identity, student_record))


# mutablity demo(update, age)
student_record["age"] = age + 1
print("update age :", student_record["age"])

#display all students
for identity, record in students:
    print(f"\nid: {identity[0]}, dob: { identity[1]}")
    print(f"\nName: {record['name']}, Age: {record['age']}, Grade : {record['grade']}")
    print("subjects:",",".join(record['subject']))