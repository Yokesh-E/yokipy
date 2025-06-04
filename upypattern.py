  """
a=6
for i in range(1,a+1):
    for j in range(1,i+1):
        print("i=",i,"j=",j,end=" ")
    print()
       
"""
"""
#reverse
a=6
for i in range(a+1,1,-1):
    for j in range(1,i):
        print("*",end=" ")
    print()
"""
"""
a=6
for i in range(1,a+1):
    for j in range(1,i+1):
        print(chr(64+i),end=" ")
    print() 
A 
B B 
C C C 
D D D D 
E E E E E 
F F F F F F
"""
"""
a=6
for i in range(1,a+1):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()

A 
A B 
A B C 
A B C D 
A B C D E 
A B C D E F
"""
"""
a=6
for i in range(10):
    if a%i==0:
        c=i
"""        
"""
a=6
for i in range(1,a):
    print(" "*(a-i) + "* "*(i))
  
 """  
"""
a=6
for i in range(1,a+1):
    print(" "*(a-i),end="")
    print("* "*i)"""
"""
a=6
for i in range(a):
    print(" "*(i) + "* "*(a-i))
"""
"""
a=6
for i in range(1,a+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

for l in range(a+1,1,-1):
    for k in range(1,l):
        print("*",end=" ")
    print()
"""
"""
a=6
for i in range(a):
    print(" "*(a-i),end=" ")
    for j in range(i):
        print("* ",end=" ")
    print()

for i in range(0,a):
    print(" "*i,end=" ")
    for j in range(a-i):
        print("* ",end=" ")
    print()    
 """

a=6
for i in range(a):
    for j in range(i+1):
        print("*",end="")
    print()    
    

