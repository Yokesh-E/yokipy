"""
a=[10,12,-5,0,6,11,-4,-8]
a2=0
a3=0
a4=1
for i in a:
    if i>=0:
        a2+=1
    elif i<0:
        
        a3+=1
    else:
        a4+=1
 
print("total possitive is",a2)        
print("total -ve is",a3)        
print("total 0's is",a4)       
"""
    
"""
a=[10,12,-5,0,6,11,-4,-8]
a2=0
a3=0
a4=1
for i in a:
    if i%2==0:
        a2+=1
    elif i!=0:
        
        a3+=1
    else:
        a4+=1
 
print("total even no",a2)        
print("total add is",a3)        
print("total 0's is",a4)          

"""
"""
a=5
b=2
print(f"{a} is greater than {b}")
"""
"""
for i in range(12):
    print("i=",i)
    for j in range(10):
        print("j=",j)
"""
"""
a=1234567
s=str(a)
b="banana"
for i,j in zip(s,b):
    print(i,j)
"""
"""
a=1234567
b="banana"
s=str(a)
for i in s:
    for j in b:
        print(i,j)"""
"""
a=[3]
#for i in a:
for i in range(3,4):
    for j in range(11):
        print(i,"x",j,"=",i*j)
    print()    
     """
"""
a="Banana"
b="britania"
c="maintain"
a1=0
for i in a:
    for j in b:
        for z in c:
            a1+=1
            print(z,j,end=" ")
            
    print(i)
    print(a1)
    print()
    
"""

a=" hi hello yokesh how are you"
b=a.split()
c=len(b)
print(b)
d=[]
for i in range(c):
    for j in range(1,c):       
        
        if b[j] > b[i]:
            a1=b[j]
            
print(a1)            
        
        
    
    
