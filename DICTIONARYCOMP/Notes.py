##### DICTIONARY COMPREHENSION #####
    # new_dict = {new_key:new_value for item in list}
    
    # new_dict = {new_key:new_value for (key,value) in dict.items()}
        # Loops through each of the key items and value items in the already existing dictionary
        
    # new_dict = {new_key:new_value for (key, value) in dict.items() if test}
        # Condition
        
import random 
names = ["Andrew", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# new_dict = {new_key:new_value for item in list}
student_scores = {student:random.randint(1,100) for student in names}
print(student_scores)

passed_students = {student:score for (student,score) in student_scores.items() if score >= 60}
print(passed_students)
