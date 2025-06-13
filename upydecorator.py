#decorator

"""
def inner():

    print("hi")
def b():
    print("lo")
inner()
b()
print(inner)
print(b)

#reference passing parameter

def inner():

    print("hi")
def b(a): #reference passing parameter
    a()
    print("lo")
b(inner)


def a(x,y):
    return x+y
def di(ref,x,y):
    return ref(x,y)
r=di(a,6,7)
print(r)
    

def a(x,y):
    print( x+y)
    def m(x,y):
        print(x*y)
        def r(re,x,y):
            return re(x,y)
        return r()

def a(x,y):
    return x+y
def m(x,y):
    return x*y
def di(ref,x,y):
    return ref(x,y)
r=di(a,6,7)
print(r)
r=di(m,6,7)
print(r)

def u(x):
    return x.upper()
def l(x):
    return x.lower()
def r(re,x):
    return re(x)
j=r(u,"yoko")
k=r(l,j)
print(j,k)


def u(x):
    def p():
        val=x()
        return val.upper()
    return p
def di():
    return "hi"
res=u(di)
print(res())
        

def upper(text):
    def process():
        val=text()
        return val.upper()
    return process
def lower(text):
    def process2():
        val=text()
        return val.lower()
    return process2

def display():
    return "welcome home"
res= (lower(upper(display)))
print(res())



def upper(text):
    def process():
        val=text()
        return val.upper()
    return process
def lower(text):
    def process2():
        val=text()
        return val.split()
    return process2

@lower
def display():
    return "welcome home"
print(display())


def dec(rf):
    def wr():
        print("hi")
        rf()
        print("free")
    return wr
@dec
def tr():
    print( "hello")
tr()


def dec(rf):
    def wr():
        print("hi")
        rf()
        print("free")
    return wr

def dec1(rf):
    def wr1():
        print("hii")
        rf()
        print("frees")
    return wr1
@dec
@dec1
def tr():
    print( "hello")
    print( "python")
tr()
"""
def addr(gui):
    def add1(a,b):
        return gui(a,b)
    return add1
##def eve(gui):
##    def eve1():
##        val=gui()
##        print(val-3)
##    return eve1

@addr
def ing(x,y):
    return x+y
print(ing(5,5))
