"""
#anagram question
a="lopetn"
b="bslent"
n=0

if len(a)==len(b):
    for i in a:
        if i in b:
            n+=1
        else:
            print("its not anagram")
            break
            
else:
    print("its not anagram")
if n==len(a):
    print("its anagram")
    

#remove dublicate values
l=[1,2,2,3,4,5,5,6,7,4]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
            
print(l1)
    

#find max element then befre element

a="hi helo aokesh barman Muthukrishnan sn"
b=a.split()
l=""
for j in b:
    if len(j)>=len(l):
        l=j    
for i in b:
    if len(i)>=len(l):
        print(i)
        break
           


a="hello world"
print(a[10:0:-9])
print(a[8:3:-2])
print(a[10:1:-4])
print(a[8:6:-1])
print(a[-1:-12:-10])


num=[2,2,2,4,3,2,2]
l=0
for i in num:
    if i%2!=0:
       l=i
       num.remove(i)
print(num)
print(l)


"""
