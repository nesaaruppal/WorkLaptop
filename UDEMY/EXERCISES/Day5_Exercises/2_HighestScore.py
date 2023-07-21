print("Calculate the Highest Score!")

high_score = 0 

student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
num_scores = len(student_scores)

for score in student_scores:
    if score > high_score:
        high_score = score
        
print(f"The highest score in the class is: {high_score}.")
    