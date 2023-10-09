# new_dict = {new_key: new_value for item in list}

# new_dict = {new_key: new_value for (key, value) in dict.items()}

# new_dict = {new_key: new_value for (key, value) in dict.items() if test}
import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

new_dict = {student:random.randint(1,100) for student in names}
print(new_dict)


#NEW DICTIONARY USING A DICTIONARY 
passed_students = {student:score for (student, score) in new_dict.items() if score >= 60}
print(passed_students)


#Looping through dictionaries
student_dict = {
    "student": ["Ben", "James", "Jack"],
    "score": [56, 78, 98]
}

for (key, value) in student_dict.items():
    print(value)
    print(key)

# Create a DF from a Dictionary 
import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through DataFrame
for (key, value) in student_data_frame.items():
    print(key)
    print(value)
    
# Loop through rows of the DF
for (index, row) in student_data_frame.iterrows():
    print(row)
