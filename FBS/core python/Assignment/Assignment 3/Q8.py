import random
id=input("enter the id:")
passs=input("enter the password:")

username="admin"
password="admin"

if(id==username and passs==password):
    systemcode=random.randint(1,10000)
    print(systemcode)
    captcha=int(input("enter the captcha:"))
    if(captcha==systemcode):
        print("login successful")
    else:
        print("captcha is incorrect")
else:
    print("username or password is incorrect")
