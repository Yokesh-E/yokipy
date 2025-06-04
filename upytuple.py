"""
l=(1,2,3,4,5)
l[2]=6
print(l)
l1=(1,2,3,4,5)
l1[2]=6
print(l1)
"""
"""
t1=(1,2,(3,4),5)
print(t1[2])
t2=(1,2,"kamal",(77,91),46,81,(95))
print(t2[4])
print(t2[:5])
print(t2[-1:-4])
"""
"""
t=(1,2,3,4,5)
l=list(t)
l[2]=6
t=tuple(l)
print(t)
"""
"""
t1=(1,2,(3,4),(5),(6,7),8,9,(11),12)
l1=list(t1)
l2=list(t1[4])
l2[1]=14
l1[4]=tuple(l2)
t1=tuple(l1)
print(t1)

"""
"""
t1=(1,2,3)
t2=(4,5,6)
t3=t1+t2
print(t3)

t3=(1,2,3)
print(t3*2)
"""

"""
t1=(1,2,3,4,5)
(red,*blue,black,green)=t1
print(red)
print(blue)

t2=(1,2,3,4,5,6,7)
(one,*two,three)=t2
print(one)
print(two)
print(three)
"""
"""
t1=(1,2,3,4,5)
t3=t1.index(2)
print(t3)
"""
"""
a=(1,2,(3,4),5,6,(7,8),9)
l=list(a)
l1=list(l[2])

l.pop(2)
for i in range((len(l1))-1,-1,-1):
    l.insert(2,l1[i])
l2=list(l[6])
l.pop(6)
for j in range (len(l2)-1,-1,-1):
    l.insert(6,l2[j])
print("list=",l)
a=tuple(l)
print("tuple=",a)
"""
"""
a=(1,2,(3,4),5,6,(7,8),9)
l=list(a)
l1=[]
for i in l:
    if type(i) is tuple:
        for j in i:
            l1.append(j)    
    else:
        l1.append(i)
print(tuple(l1))
    
"""

