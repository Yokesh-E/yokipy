"""
#map():
to compaining the work data structure in iterable value given operation
syntex:
map(function name,iterable)

a=[1,2,3,4,5,6]
b=[]
for i in a:    
    b.append(i+i)
print(b)

a=[1,2,3,4,5,6]
def adde(b):
    for i in b:
        print(i+i)
adde(a)
#maping
def add(n):
    return n+n
number=(1,2,3,4,5)
res=map(add,number)
print(list(res))

num=(1,2,3,4,5)
res=map(lambda x:x+x,num)
print(list(res))

num="hi"
res=map(lambda x:x.upper(),num)
print(list(res))

def add(n):
    return n.upper()
m=["fun","make"]
m1=[]
for i in m:
    m1.append(add(i))
print(m1)


a="yokesh"
b=[]
for i in a:
    b.append(i.upper())
print(b)

a=[1,2,3,4,5,6,7,8,9,10]
def eve(n):
    if n%2==0:
        return n
c=map(eve,a)
print(list(c))

#filter

a=[1,2,3,4,5,6,7,8,9,10]
def eve(n):
    if n%2==0:
        return n
c=filter(eve,a)
print(list(c))

a=lambda x:"hi" if x>0 else "no"
print(a(10))

a=[1,2,3,4,5,6,7,8,9,10]
c=filter(lambda x:x%2==0 ,a)
print(list(c))

a=(1,2,3,-2,5,-9,-4,-5)
c=filter(lambda x:x>=0,a)
print(list(c))


a="abbbccccvvddxxyyuuooppll"
b=set(a)
print(b)
l=""
for i in sorted(b):
    n=0 
    for j in a:
        if i==j:
            n+=1                
    print(i+""+str(n),end=" ")

        
#pip install fastapi
#pip install uvicorn

#zip()


a=(1,2,3,4,5)
b=(6,7,8,9,10)
d=(11,12,13,14)
c=zip(a,b)
print(dict(c))

a=(1,2,3,4,5)
b=(6,7,8,9,10)
d=(11,12,13,14)
c=zip(a,b,d)
e={i:(j,k)for i,j,k in c}
print(e)

a=[1,2,3,4,5]
b={6,7,8,9,10}
c=(11,12,13,14)
d=zip(a,b,c)
print(list(d))
f={i:j,k for i,j,k in d}
print(f}


a={"one":["a","b","c"],"two":["d","e","f"]}
b={"three":["g","h","i"],"four":["k","l","m"]}
c=zip(a,b)
print(a["one"])
print(list(c))
v={}
for i in a:
    d=
   
   
#enumerate()

a=["apple","banana","orange","mango"]
c={i:j for i,j in enumerate(a,start=2) }
print(c)

a={"1","2","3"}
b={1:"apple",2:"mango",3:"kiwi"}
d={i:j for i,j in zip(a,b.items())}
print(d)

#eval()

a="2"
b="6"
print(a+b)
c=8
d=4
print(eval("c+d"))


l=5
a="5+10*2+6+l"

a=eval("[x*2 for x in range(5)]")
print(a)


#reduce()
#syntax
#reduce(functin,iterable,initializer value)

from functools import reduce
num=[1,2,3,4,5]
res=reduce(lambda x,y: x+y,num,5)
print(res)

from functools import reduce
num=[1,2,3,4,5]
res=reduce(lambda x,y: x*y,num)
print(res)

from functools import reduce
num=[1,2,3,4,5]
gh=["hello","world","python"]
l=reduce(lambda x:x+x for x in gh)
print(l)
"""