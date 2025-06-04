"""
def greet(a,b):
    print(a+b)
    print(a*b)
    print(a/b)
    print(a//b)
print(greet(5,10) ) 
print("no worry")
"""

def login():
    uname=input("enter name:")
    passw=int(input("enter pass:"))
    if uname=="kamal" and passw==12345:
        print("valid")
    else:
        print("in valid")
login()
