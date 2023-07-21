print("Average Height Calculator!")

student_heights = [180, 124, 165, 173, 189, 169, 146]
num_students = len(student_heights)

height = 0 

for student in student_heights:
    height += student
    
average_height = round(height / num_students)

print(average_height)