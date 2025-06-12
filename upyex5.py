"""
a={1:1,2:2}
b={}
b=dict.copy(a)
print(a[1])
print(b)

a=5
n=0
for i in range(a): 
    for j in range(i):
        print(n,end=" ")
        n+=1
    print()


def e(a,c):
    print(a+c)
    def h(b,d):
        print(b*d)
        def j(k,l):
            return k-l
        return j
    return h #dont use ()
closure=e(5,3)
el=closure(2,3)(2,3)
print(el)
print(e(5,3)(2,3)(2,3))

a=10
def l():
    a=12
    def d():
        nonlocal a
        a=13
        print(a)
    
    d()
    print(a)
    
l()
print(a)

def e(a,c):
    print(a+c)
    def h(b,d):
        print(b*d)
        def j(k,l):
            return k-l
        return j
    return h #dont use ()
closure=e(5,3)(1,2)(1,2)
print(closure)

a=eval("4")
b=eval("8")
print(a+b)
"""
a="aaabaa"
b=list(a)
print(b[0])
c=list(a)
for i in range(len(b)):
    n=0
    for j in range(len(c)):
        if b[i]==c[j]:
            n+=1
            b.remove(c[i])
        else:
            break
    print(a[i],n,end="")

