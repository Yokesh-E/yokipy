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
"""
a=(1,2,3,-2,5,-9,-4,-5)
c=filter(lambda x:x>=0,a)
print(list(c))
