#iterator
"""

a={1,2,3,4,5}
b=0
while b<len(a):
    print(a[b])
    b+=1

a={1,2,3,4,5}
for i in a:
    print(i)
    

a={1,2,3,4,5}
b=iter(a)
print(next(b)) #or print(b.__next__())
print(next(b))
print(next(b))
print(b.__next__())

a=[1,2,3,4,5]
b=iter(a)
print(next(b)) #or print(b.__next__())
print(next(b))
print(next(b))
print(b.__next__())

a=(1,2,3,4,5)
b=iter(a)
print(next(b)) #or print(b.__next__())
print(next(b))
print(next(b))
print(b.__next__())
print(b.__next__())
print(b.__next__())#extra print its gives error n value
print(b.__next__())

a={1:1,2:2,9:3,4:4}
b=iter(a)
print(next(b)) #or print(b.__next__())
print(next(b))
print(next(b))
print(b.__next__())

a={1:1,2:2,9:3,4:4}
b=iter(a)
for i in b:
    print(i)


#generator

def generate():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6
gen=generate()
print(gen.__next__())
print('k')
for i in gen:
    print(i)
    


def demo():
    n=1
    while n<=4:
        l=n*n
        yield l
        n+=1
a=demo()
for i in a:
    print(i)


def demo():
    n=1
    while n<=4:
        l=n*n
        return l
        n+=1
a=demo()
for i in a:
    print(i)

def demo():
    n=1
    while n<=4:
        l=n*n
        
        n+=1
        return l
a=demo()
print(a)
"""
l=(x*x for x in range(5))
print(next(l))
print(next(l))

#genrator only works on only tuple data type in comprehension
#normally works all data types
l=[x*x for x in range(5)]#its not work
print(next(l))
print(next(l))
