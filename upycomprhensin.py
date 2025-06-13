# comprehension

#[ expression for item in iterable if cndition]
"""
print([x**2 for x in range(1,6)])
print([x**2 for x in range(1,6) if x%2==0])
print({x**2 for x in range(1,6) if x%2==0})

a=set()
for i in range(1,20):
    if i%2==1:
        b=i**2
        a.add(b)
print(a)        


a={x+x : x**2 for x in range(1,20)}
prin(a)

a={-5,-4,5,6,8,10}
b={x+5 for x in a if x>0}
print(b)

#cartition product join method
print([(a+1,b+2)for a in range(2) for b in range(2)])

a="helloworld"
print([i.upper() for i in a if i not in "o"])

a="helloworld"
b=[]
for i in a:
    if i not in "o":
        b.append(i)

print(b
"""
a=[[1,2,[3,4],5,6,[7,8],[9]]]
b=[x for i in a  for x in  i if isinstance(x,int)]
print(b)
##for k in a:
##    for l in k:
##        
##        print(l)

for i in a:
    
    if i is list:
            for k in i:
                print(k)
    print(i)
