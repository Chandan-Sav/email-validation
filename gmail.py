email=input("Please enter your e-mail:")
k,r,s=0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if("@"in email) and (email.count("@")==1):
            if (email[-4]==".") ^ (email[-3]=="."):
                for a in email:
                    if a==a.isspace():
                        k=1
                    elif a.isalpha():
                        if a==a.upper():
                            r=1
                    elif a.isdigit():
                        continue
                    elif a=="_" or a=="@" or a==".":
                        continue
                    else:
                        s=1
                    if k==1 or r==1 or s==1:
                         print("Space error !!you have entered an unexpected space in address.")
            else:
                print("Wrong Domain address.!!")
        else:
            print("A '@' is symbol is exceeding in ur email address.")
    else:
        print("Wrong Character identified! Please enter valid character")
else:
    print("Oops!! Please enter valid email id. :)")