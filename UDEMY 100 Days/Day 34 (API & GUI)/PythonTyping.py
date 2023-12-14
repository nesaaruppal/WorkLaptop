# Can set a constant data type 
    # age: int
    # name: str
    # height: float
    # is_human: boolean
    
age: int
# Now the age has to match the data type specified
age = 12

def police_check(age:int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return "Hello"


print(police_check(21))
        