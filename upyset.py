"""
s1={1,2,3,10,4,5,6}
s={1,"two",True,False,0}
l=[1,"two",True,False,0]
print(s)
print(l)
"""
"""
s1=set((1,2,3,45,4))
s2=set([55,6,7,8,9])
print(s1)
print(s2)
"""
#adding method add,update
"""
s1=set((16,1,2,3,45,4))
l=list(s1)
l[2]=4
print(set(l))
"""
"""
s1={1,2,3}
s2={4,5,6}
s1.add(8)
s1.update(s2)
print(s1)
s3=[14,12,6]
s1.update(s3)
print(s1)
s4=(18,19,13)
s1.update(s4)
print(s1)
"""

#remove method remove(),discard(),pop(),clear(),del()
"""
s={1,2,3,4,5}
s.remove(4) #same discard()
print(s)
"""
"""
s={1,2,3,4,5}

s2=s.pop()
print(s2)

#clear
s1.clear

#del()
del s1

"""
"""
#in build methos
#union
s1={1,2,3}
s2={4,5,6}
s4={7,8,9}
s3=s1|s2|s4 #s3=s1.union(s2,s4)
print(s3)
"""
"""
#intersection
s1={1,2,5,3}
s2={4,5,6}
s4={7,8,9}
s3=s1&s2 #s3=s1.intersection(s2)
print(s3)
"""
"""
#intersection_update
s1={1,2,5,3}
s2={4,5,6}
s4={7,8,9}
s1.intersection_update(s2)
print(s1)
"""
"""
#difference(-)
s1={1,2,5,3}
s2={4,5,6}
s3=s1- s2 #s3=s1.difference(s2)
print(s3)
"""
"""
#difference_update
s1={1,2,5,3}
s2={4,5,6}
s1.difference_update(s2)
print(s1)
print(s2)
"""
"""
#symetric difference(^)
s1={1,2,5,3}
s2={4,5,6}
s3=s1^s2
print(s3)
"""
"""
#symmetric_difference_update
s1={1,2,5,3}
s2={4,5,6}
s1.symmetric_difference_update(s2)
print(s1)
print(s2)
"""
"""
#issuperset
s1={1,2,5,3}
s2={4,5,6}
s3=s1.issuperset(s2)
print(s3)
"""
"""
#issubset
s1={1,2,5,3}
s2={4,5,6}
s3=s1.issubset(s2)
print(s3)
"""

"""
a={77,99,(66),7,88,(76,75,76),97}
l=list(a)
l1=[]
for i in l:
    if type(i) is tuple:
        for j in i:
            l1.append(j)
    else:
        l1.append(i)

print(set(l1))
"""

"""
how interpreter works
lexing
passing
ast
compilation
byte code
pvm(py virtual machine)
binary code
"""

a=4
print("*"*a,end="")
print()
for i in range(a):
    for j in range(a):
        print("l"*j,end="")
    for k in range(a,0,-1):
        print("*"*k,end="")
    

