"""
#4th question

n=int(input("Enter no="))
for i in range(1,n+1):
    if i%3==0 and i%5==0:
        print(i,"FizzBuzz")
    elif i%3==0:
        print(i,"Fizz")
    elif i%5==0:
        print(i,"Buzz")

       

#5th question

a=[1,2,3,4,5,6,7,8,10]
n=int(input("enter no"))
l=[]
for i in range(1,n+1):
    if i not in a:
        l.append(i)
    
print(l)       

#6th question

num=[2,2,2,3,2,2]
l=0
for i in num:
    if i%2!=0:
       l=num.pop(i)    
print(num)
print(l)



#7th question

a="I am a python i am a popular programming language"
b=a.split()
for i in range(len(b)-1,-1,-1):
    print(b[i],end=" ")



#8th question

a="listen"
b="silent"
if sorted(a)==sorted(b):
    print("its anagram")
else:
    print("its not anagram")

  

# 9th question

a=[10,20,15,11,12,13,14,15,18,19]
l=0
for i in a:
    if i%2==0:
        l+=i
print(l)        




#10 question

a="i am a software developer"
b="aeiou"
print(len(a))
c=0
for i in b:
    for j in range(len(a)):
        if i==a[j]:
            c+=1
print(c)            
        


#11th question
l=[1,2,2,3,4,5,5,6,7,4]
s=set(l)
l=list(s)
print(l)

#12th question

a=int(input("enter no="))
for i in range(1,11):
    print(i,"x",a,"=",i*a)
"""
