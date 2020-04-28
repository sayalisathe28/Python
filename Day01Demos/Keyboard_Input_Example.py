"""
Keyboard input

1. raw_input()
2. input()
"""

name = raw_input("Enter Your Name") #name will be String
print "Hello ",name
print "Type of name = ",type(name)

if type(name)==str: #boolean value in python are True and False
    print "Yes String...."
else:
    print "No it is not a string..."

s1="100"
num=int(s1) #conversion
num1=100
print num1==num #True

"""
Assignment
    1: Accept a string by raw_input()
        get upper string
        get lower string
        check if this input contains only alphabetical content
        and then check if it is lower case
    2: Accept a string, check if it is a valid password "psl"
    3. Accept a string, check whether it is palindrome
"""
