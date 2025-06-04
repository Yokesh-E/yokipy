"""a=10.5
b=20+5j
c=30.4

d=str(b)

print(complex(c))
print(type(d))
print(d)"""

#input

"""a=input("enter")
print(a,type(a))
b=int(input("enter"))
print(b,type(b))"""
#a,b=(list(input("a="))),(set(input("b=")));print( a,b)
"""a=("a",)
b=("a")
c="a"
print(a,type(a))
print(b,type(b))
print(c,type(c))"""

#operators

"""a=16
b=11
c=10
d=16

e=(a**b)+(c//d)
print(e)"""

#comparison

"""a=str(input("a="))
b=str(input("b="))
c=(a==b)
print(c)"""
"""a={1}
print(a,type(a))"""

"""a="10"
b="10"
print(a!=b and b!=a or a==b)"""

"""c="yokesh"
d="musthafa"
print(d!=c or c==d and c!=d)"""

"""a=12.15
b=15.12
c=6.8
d=12.15
print(a!=b or a==b and c!=b or d==a and b==c)
print(a!=b or a!=d and c!=b or d==b and b==c)
print(a!=b and a==b)"""

"""f=16
f+=16
print(f)
f*=2
f//=2
print(f)
print(f)"""

#assignment operator

"""a=10
b=20
c=a
print(a is c)
print(a is b)
print(a==b)
print(a==c)
print(c)"""
"""a=10
b=a
c=10
print(a is c)
print(a is b)
print(a==b)
print(a==c)
print(c)"""

"""a=[1,2,3,4]
b=a
c=[1,2,3,4]
print(a is c)
print(a is b)
print(c is b)
print(a==c)
print(a==b)
print(b==c)
print(id(a))
print(id(b))
print(id(c))"""

#membership operator

"""a="hello python"
print("o" in a)
print("i" in a)
b=[10,10]
print(0 in b)
print(1 in b)

c=["banana","mango","graphs"]
print("mango" in c)
print("a" not in a[0])"""

"""a={"name":1,
   "name2":2,
   "name3":3}

print(1 in a)
print("name" in a)"""

#bittwise perator

"""a=256
b=100
print(~a,a
a=10.3//3
print(a))"""

#important

#string method

"""a="python".upper()
print(a)
a1="PYTHON".lower()
print(a1)
a3="i am yokesh".swapcase()# small into cap,cap into small
print(a3)
a4="i learn python".title()
print(a4)
a5="i learn python".capitalize()
print(a5)
a6=" i learn py"
print(a6)
b="python"
print(max(b))
b1="PyThOn"
print(max(b1))
print(ord("y"))
b2="python"
print(ord("h"))
print(min(b2))
c="i learn python"
print(c.split())
d="i learn python"
d1=d.replace("python","java")
print(d1)
d2=" i learn python".replace(" ","_")
print(d2)"""
"""a="python"

print(a.isdigit())
a1="python"
print(a1.isdigit())
a3="123" 
print(a3.isdigit())"""

"""a="python"
print(a.isalpha())
a1="python123"
print(a1.isalpha()) """

"""a=" "
print(a.isspace())
a1="i learn python"
print(a1.isspace())"""

"""a="python"
print(a[3])
print(a[-3])
print(a[1:4])
print(a[ :-2])
print(a[-4:-2])
print(a[::-1])
print(a[::2])
#priint(a[start:end:step])
print(a[5:2:-1])
print(a.count("p"))

text=("abcdefghijklmnopqrstuvwxyz")
print(text[::-1])
print(text[-1:-9:-1])
b=("".join(reversed(text)))
print(b)"""

"""c="hello1"
print(c.strip("_"))
print(c.strip(" e"))""" #its works start and end

#to find index position in string

"""word="helloo python"
print(word. find("n")) #12

a="hello"
print(a[-3:5:2])
print(a[-3:3])"""

#control flow statement

"""a="4"
if (a<2 or a==4):
    print("HI")
print("jk")"""

"""age=int(input("enter age:"))
if age>=18:
     print("ok")"""

"""username=input("enter name:")
password=input("enter pass:")
if (username=="kamal" and password==12345):
    printt("access accept")
else:
    print("denied") #its output is else statement"""
"""
a="apple"
b="mango"
if ('a' in a and 'i' not in a or a!=b and a==b):
    print("its wrong stament")
else:
    print("its correct")"""

"""a1=2
a2=4
if (a1==a2 and a1!=a2 or a1!=a2 and a1==a2 and a1!=a2):
    print("correct")
else:
    print("wrong")"""
"""
a="musthafa"
b=12
age=23
if ("s" not in a):
    if (a!=B):
        print("crrect")
else:
    print("wrong")"""

"""a=("suresh kumar")
if("u" in a):
    print("u")
if("h" in a):
    print("h")
if(" " in a):
    print("space")
if ("r" in a):
    print("r")
    if ("z" not in a):
        print("z")
print("suresh kumar") """

#elif statement(elif inside not allow agan elif

"""a=("suresh kumar")
if("u" in a):
    print("u")
elif("h" in a):
    print("h")
elif(" " in a):
    print("space")
elif ("r" in a):
    print("r")
    if ("z" not in a):
        print("z")
else:        
  print("suresh kumar")
    """

"""mark=int(input("enter mark :"))

if mark<=50 and mark >40:
    print("f grade")
elif mark > 50 and mark <60:
    print("E Grade")
elif mark >= 60 and mark <70:
    print("D Grade")
elif mark >= 70 and mark <80:
    print("C Grade")
elif mark >= 80 and mark <90:
    print("B grade")
elif mark >=90 and mark <101:
    print("A Grade")
elif mark >100:
   print ("apsara pencil")
else:
    print("fail")"""
"""
food=input("food name :")
menu=("curd","tomato","veg","lemon")
if food in menu:
    print("food is available")
else:
    print("sorry not available")
print(type(menu))
"""
"""
a="good bad"
b="sarkar"
c="maanadu"
d=c
if('o' in a and 'd' in a):
    print("this is corrected")
    if (a!=d and a is d):
        print("not coorected")
    elif(c==a or a!=c):
        print("corrected")
        if (b!=a and b==c):
            print("all the output")
        else:
            print("this is printed")
    else:
         print("this code is terminated")
else:
    print("control flow statement is ended")
    
    """


year=int(input())
if(year%4==0 and year%100!=0)or (year%400==0):
    print("leap")
else:
    print("not")
print(2024%400)
    

        
    
