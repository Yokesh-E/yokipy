"""
#namespacing varibale rules in py

#global
a=10
def b():
    global a
    print(a)
b()#10

a=10
def b():
    global a
    a=5
    print(a)
b()# 5

#local
def b():
    a=5 # its local
    print(a)
b()

#enclosing
#outer and inner data combained assign var values
b=2
def a():
    b=10
    print(b)
    def b():
        b=15#its enclosing
        return b
    
    print(b())
a()

a=10

def hii():
    
    b=15
    a=12
    print(a)
    c=1    
    def he():
        nonlocal a
        c=100
        print(c)    
    he()
    print(c)
hii()

#closure
def e(a):
    def h(b):
        return a+b
    return h(7)
print(e(5))

def e(a):
    def h(b):
        return a+b
    return h #dont use ()
closure=e(4)
res=closure(5)
#print(res)
print(e(8)(2))

def e(a,c):
    print(a+c)
    def h(b,d):
        print(b*d)
        def j(k,l):
            return k-l
        return j
    return h #dont use ()
closure=e(5,3)
print(closure(6,5)(3,4))
print(e(5,3)(6,5)(3,4))#not using(),()

def e(a):
    print(a)
    def h(b):
        print(b)
        def j(k):
            return k
        return j
    return h #dont use ()
closure=e("hi")
print(closure("hello")("python"))


def g(a):
    print(a)
    def h(b):
        print(b+5)
    return h(a)
print(g(10))

def addmul(a,b):
    def add(a,b):
        return(a+b)
    def mul(a,b):
        return a*b
    return add, mul
x,y=addmul(6,5)
print(x(2,3))
print(y(4,5))

def wel():
    def come(s):
        return s.title()
    return come
pi=wel()
print(pi("hi"))

def g(x):
    def h(y):
        return x**y
    return h
s=g(4)
c=g(7)
print(s(6))
print(c(6))

def d(x):
    def f(c):
        c+=1
        print(c)
    return f(x)
g=d(5)
print(g)
print(g)

def inc(start=0):
    
    co=start
    def hi():
        nonlocal co
        co+=1
        return co
    return hi
j=inc(6)
print(j())
print(j())
print(j())

def myaccount(initial_balance):
    balance=initial_balance
    
    def deposit(amount):
        nonlocal balance
        balance+=amount
        return balance
    def withdraw(amount):
        nonlocal balance
        balance-=amount
        return balance
    def get_balance():
        
        return balance
    return{"deposit":deposit,"withdraw":withdraw,"get_balance":get_balance}
account=myaccount(100)
print(account["deposit"](50))
print(account["withdraw"](20))
print(account["get_balance"]())
        
"""  

