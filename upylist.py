"""
l1=["1","2","3"]
l1.append("apple")
print(l1)
l1.extend("apple")
print(l1)
l2=["5ajk","6"]
l1.extend(l2)
print(l1)


for i in l2:
    l1.append(i)
print(l1)

"""
"""
l1=["1","2","3"]
l2=["5ajk","6"]
l3=["hjjk","jijmm"]
for i in l2:
    l1.append(i)
for j in l3:
    l1.append(j)
print(l1)
"""
"""
l1.append(l2,l3)#error because only one argument is possibl in append
print(l1)
"""
"""
l1=["1","2","3"]
l2=["5ajk","6"]
l3=["hjjk","jijmm"]
l1.insert(1,"O")#(index,value)
print(l1)

#remove list
#remve(),pop(),clear(),del()
"""
"""
a=5
l=[]
p=0
for i in range(a,0,-1):
    p+=i
    l.append(i)
print("total=",p)
print(l)
  """
"""
a=5
l=[]
p=0
for i in range(a,0,-1):
    p=i**2
    l.append(p)
print(l)    

"""

   

    



    
