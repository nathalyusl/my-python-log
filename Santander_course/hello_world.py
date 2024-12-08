print("Hello, World!")

"""
Conditional Structures 
"""
# IF
age = 18

if age >= 18:
    print("You are an adult.")

#IF - ESLSE

age = 15

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# IF-ELIF-ELSE

grade = int(input("Grade: "))

if grade >= 90:
    print("Excellent")
elif grade >= 80:
    print("Very good")
elif grade >= 70:
    print("Good")
else:
    print("Needs improvement")