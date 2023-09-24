# This is a comment

name = "Sarah" # This is an inline comment
print(name)
print(type(name))
print(type(name) == str) # prints true because name is a string
print(isinstance(name, str)) # prints true because name is a string

# other types include: int, float

# You can force an int to be a float with
age = float(25)

# You can force a variable to be an int with
ageInt = int("25")

# complex for complex numbers
# bool for booleans
# list for lists
# tuple for tuples
# range for ranges
# dict for dictionaries
# set for sets

# Arithmetic Operators
# % boolean
# ** exponent
# // division and rounds down 5 // 2 = 2

# operators
# ==, !=, >, <=

# boolean operators
# not = !
# or = ||
# and = &
# is = used to compare objects, returns true if both objects are the same

def is_adult(age):
    if age > 18:
        return True
    else:
        return False
def is_adult2(age):
    return True if age > 18 else False

print("""I
      
      am
      writing on a multiline 
      
      string""")

# string.upper() string.lower() string.title() string.islower() string.startswith() string.endswith()
# string.strip() = string.trim()

# len(string) = string.length()