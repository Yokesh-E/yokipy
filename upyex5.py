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
"""
