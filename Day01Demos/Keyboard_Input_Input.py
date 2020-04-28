"""
Keyboard input

1. raw_input()
2. input()
"""

name = input("Enter Your Name") #name will be String
print "Hello ",name
print "Type of name = ",type(name)

input(

"""
Execution :

Case 1:
    Enter Your Name100
    Hello  100
    Type of name =  <type 'int'>

Case 2:
    Enter Your Name3.14
    Hello  3.14
    Type of name =  <type 'float'>
    
Case 3:
    Enter Your NameABC

    Traceback (most recent call last):
      File "H:/ELTP_Python/Day1_Demos/Keyboard_Input_Input.py", line 8, in <module>
        name = input("Enter Your Name") #name will be String
      File "<string>", line 1, in <module>
    NameError: name 'ABC' is not defined

Case 4:
    Enter Your Name"ABC"
    Hello  ABC
    Type of name =  <type 'str'>

Case 5:
    Enter Your Name4+5
    Hello  9
    Type of name =  <type 'int'>
"""
