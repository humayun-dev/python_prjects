# Email validation using regex module. Following are the rules for the email creation
'''
    a-z, 0-9, 
    The dot(.), @ and _ should be once in the email
    The dot(.) should be at position 2 or 3
'''
import re   # import regex module

'''
    ^ = starting point
    + = concatenation
    \ = search
    ? = only one, so [\._]? means that search the dot and underscore and it should occur only once
    \w = search through string
    $ = search from the back side/reverse as dot should be from the reverse side as 2 or 3
'''
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
email_input = input("Please enter email address: ")
if re.search(email_condition,email_input):
    print("Valid Email Address")
else:
    print("Invalid Email Address")