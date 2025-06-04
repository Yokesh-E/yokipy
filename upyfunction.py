"""
def greet(a,b):
    print(a+b)
    print(a*b)
    print(a/b)
    print(a//b)
print(greet(5,10) ) 
print("no worry")


def login():
    uname=input("enter name:")
    passw=int(input("enter pass:"))
    if uname=="kamal" and passw==12345:
        print("valid")
    else:
        print("in valid")
login()

#position arguments
def wel(name,age):
    print(f"hi{name}")
    print(f"u age is{age}")
wel("yoki",23)

def wel(name,age):
    name="jim"
    age=23
    print(f"hi{name}")
    print(f"u age is{age}")
#wel()#error

def wel(name,age):
    name="jim"
    age=23
    print(f"hi{name}")
    print(f"u age is{age}")
wel("yoki",23)#overwrite
#output
hijim
u age is23

# please remember  after return any other function do nt run in function

#keyword arguments
def hello(a,b):
    a=12
    return a+b
print(hello(b=12,a=10)) #output 24


def wel(name,age):
    name="jim"
    age=23
    print(f"hi{name}")
    print(f"u age is{age}")
wel(age=23,name="mersal")

#output
hijim
u age is23


def wel(name,age,gen):
    print(f"hi{name}")
    print(f"u age is{age}")
    return(gen)
wel(age=23,name="mersal",gen="male")
#output
himersal
u age is23
print(wel(age=23,name="mersal",gen="male"))
#output
himersal
u age is23
male

def lo(a,b,c):
    l=[]
    for i in range(a,b,c):
        l.append(i)
    print(l)
lo(10,1,-1)
#output
[10, 9, 8, 7, 6, 5, 4, 3, 2]

def lo(a,b,c):
    l=[]
    l1=[]
    for i in range(a,b,c):
        if i%2==0:
            print("even values")
            l.append(i)
        else:
            print("odd values")
            l1.append(i)
        
    print(l)
    print(l1)
lo(10,1,-1)

#default argument
def one(name="hi"):
    print(name)
one(" yoki") #ouput yoki

#default argument
def one(name="hi"):
    name="ki"
    print(name)
one(" yoki")#output ki

def li(a,b,c=12):
    d=a+b*c
    return d
print(li(12,10,9)) #first multiply after plus 102


def li(item="pipe",quantity,price=50):
    total=quantity*price
    return total
print(li(5)) #error

def li(quantity,item="pipe",price=50):
    total=quantity*price
    return total
print(li(5))#you first assign normal value in parameter after that assign default argument. its comes output 

def order(food, drink="tea"):
    if food == "dosa" and drink == 'tea':
        print("my order is:", food)
    elif food == "vadai" or drink == 'coffee':
        print (f"my wrong order is: {food} and {drink}")
    else:
        print("order cancel")

order(input("enter your order please:"))

# arbitrary aruments
def kl(*a):
    print(sum(a))
kl(5,5,2)#you can give multiple values 
"""
def names(*val):
    print(val) 
    for i in val:
        print(i)
print(names("hi","hello","get"))
    

