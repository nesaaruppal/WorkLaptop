print("Blackbox AI Code!")
def get_top_note(student):
    """
    Function that takes a dictionary of objects and returns a dictionary of objects
    with an additional field called 'top_note'.

    Args:
        student (dict): Dictionary of student objects with fields 'name' and 'notes'.

    Returns:
        dict: Dictionary of student objects with an additional field 'top_note'.
    """

    # Get the 'notes' list from the 'student' dictionary
    notes = student.get('notes', [])

    # Calculate the maximum note (i.e., 'top_note') in the 'notes' list
    top_note = max(notes, default=0)

    # Create a new dictionary called 'updated_student' that includes all fields from the original
    # 'student' dictionary and an additional field called 'top_note'
    updated_student = {
        'name': student.get('name', ''),
        'top_note': top_note
    }

    return updated_student

students = [
    { "name": "John", "notes": [3, 5, 4] },
    { "name": "Emma", "notes": [4, 3, 2] },
    { "name": "Sophia", "notes": [5, 5, 5] }
]

students_with_top_note = [get_top_note(student) for student in students]

print(students_with_top_note)

