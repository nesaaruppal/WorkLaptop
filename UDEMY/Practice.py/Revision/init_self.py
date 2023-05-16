# CLASS OBJECT NAMED TWEET
class Tweet:
    pass


a = Tweet()
# Objects created in this way are 'INSTANCE OBJECTS'
# Instance start with lower case
# Class names start with an upper case

# Instance objects inherit any class atributes - there are none above

a.message = "140 characters"
# You need to write the instance name and then a dot "." and then the message

# Shows what belongs to "a" and what belongs elsewhere

print(a.message)
# ABOVE WORKS

# print(Tweet.message)
# DOES NOT WORK


b = Tweet()
b.message = "A new message."

print(a.message)
print(b.message)
# These both work


# __ x __
# Referred to as hooks
# Called automatically
# __init__ is the initializer method --> it is called automattically whenever you create an instance


class Tweet:
    def __init__():
        print("hi")
        # MUST ALWAYS HAVE SELF
        # Self always refers to the particular instance
