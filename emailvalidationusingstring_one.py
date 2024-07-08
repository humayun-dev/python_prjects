# The project will validate the email based on the string functions
'''
    Concept is:
    Email is combination of e@g.com or e@g.pk, where 
    e = email, @ used once, g = gmail or any other email, . = once, com/pk = email type
    total we have 5 conditions for the email validation
'''
email = input("Enter your email: ")
k = 0 # 5th step: to check the space in the email
j = 0 # 5th step: to check the uppercase letters 
d = 0 # 5th step: any other character other than @ . _

if len(email) >= 6:     # 1st step: email possible minimum length could be 6 such as e@g.pk
    if email[0].isalpha():  # 2nd step: check email first letter as alphabet
        if ("@" in email) and (email.count("@") == 1):  # 3rd step: to check the @ character
            if (email[-4] == ".") ^ (email[-3] == "."): # 4th step: to check one dot character and negative index for checking
                for i in email:         # 5th step: to check space and capslock letter in the email
                    if i == i.isspace():    # to check the space character
                        k = 1
                    elif i == i.isalpha():  # if i is alphabets and upper letter as well
                        if i == i.upper():
                            j = 1
                    elif i.isdigit():   # if found any digit in the email, which is allowed
                        continue
                    elif i == "." or i == "@" or i == "_":  # the mentioned three characters are allowed as well
                        continue
                    else:
                        d = 1
                if k == 1 or j == 1 or d == 1:    # k is for the space,j is for the upper case letter and d = any other char
                    print("Either space, upper case letter or any character than #,.,_ in the email. Wrong email")
            else:
                print("There should be one dot character in the email")
        else:
            print("There should be one @ character in email")
    else:
        print("Email should start from alphabet letter")
else:
    print("Minimum email length should be 6")