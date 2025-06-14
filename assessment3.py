#assessment 3
"""
#1.question
l=[]
def fib(n):
    c=0
    a=1
    for i in range(n+1):
        g=c+a
        l.append(c)
        c=a
        a=g
    return l
print(fib(6))

# 2.question

def inc(l):
    
    co=l
    def hi():
        nonlocal co
        co+=1
        return co
    return hi
j=inc(10)
for i in range(5):
    print(j())


# 3.question

data=[(1,2),(2,1),(4,2)]
for i in range(1,len(data)):
    for j in data[i]:
        print(j)

        

#4.question

def gen(n):
    for i in range(n):
        yield i
    
t=gen(5)
for i in t:
    print(i)
    


  

# 5.question

def add(a,b):
    c=a+b
    print("multiply=",(a+b)*c)
    print("add=",c)   
add(1,2)


# 6.question
add=lambda a,b,c:(a+b)*c
print(add(1,2,3))


# 7.question
a=[1,2,3,4,5,6,7]
def squ(n):
    return n**2
m=map(squ,a)
print(list(m))


# 8.question

a=[1,2,3,4,5,6,7]
def eve(n):
    if n%2==0:
        return n
f=filter(eve,a)
print(list(f))


# 10.question
def a1():
    def a2(p1):
        if "12345"==p1:
            return("correct password")
        else:
            return("wrong password")
    return a2

clos=a1()
print(clos(input()))


# 11.question

def fib(n):
    c=0
    a=1
    for i in range(n+1):
        g=c+a
        yield c   
        c=a
        a=g       
t=fib(5)
for i in t:
    print(i)
    


# 12.question

def gh(hi):
    def gr(k):
        if k%2==0:
            return k
        else:
            return "not even"
    return gr
@gh
def val(n):
    return n
print(val(4))


#13.question

w=[]
def m1(h):
    def m2(j,r):
        h(j,r)      
    return m2
@m1
def val(n,f):
    for i in range(f):
        w.append(n)
    print(w)
val("hello",5)
"""


