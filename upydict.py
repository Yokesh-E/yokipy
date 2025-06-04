"""
#11 in build function there
a={"stud1":{"name":"yoki1",
   "age":23,
   "hobby":["ki","Po","lo"],
   "address":{"dict":"villu1","dt":"gige","pin":604306}},
    "stud2":{"name":"yoki",
     "age":23,
   "hobby":["ki","Po","lo"],
   "address":{"dict":"villu","dt":"gige","pin":604306}}}
print(a["stud1"]["address"]["dict"])

#
a={'stud1':{'name':"karan",
   'age':23,
   'hobbies':['cricket','coding','chess'],
   'address':{'pincode':623705,'area':'paramakudi'},
   'section':'b',
   'p_deatails':(90985674,'BATI7786')},
   'stud2':{'name':"mani",
   'age':25,
   'hobbies':['cricket','drawing','chess'],
   'address':{'pincode':6237087,'area':'ramanathapuraam'},
    'section':'a',
   'p_deatails':(9098565456,'BATI7645')}}
       
print(a)


a=dict(name="yoki",age=23,year=2002)
print(a)
print(a["name"])
        

a=[1,2,3,4,5]
a1=dict.fromkeys(a,"Not values")
print(a1)


b=(1,2,3,4,5)
b1=dict.fromkeys(b,"name")
print(b1)


b=(1,2,3,4,5)
b2="gt"
b1=dict.fromkeys(b,b2)
print(b1)

a="lion"
b="apple"
c=dict.fromkeys(a,b)
print(c)


#keys - we get the keys only on returns datas
dt={"name":"yoki","brand":"bmw","year":2026}
h=dt.keys()
print(h)



dt={"name":"yoki","brand":"bmw","year":2026}
h=dt.keys()
dt["money"]=100000000000000
print(h)
b=dt.values()
print(b)
c=dt.items()
print(c)


#pop() - to remove or eliminated particular  data
#popitem()-to eliminate end of the date on variable

a={"one":1,"two":2,"three":3}
a.pop("one")
print(a)
b=a.popitem()
print(b)

#get()- we get the data on give the keys
a={"one":1,"two":2,"three":3}
x=a.get("one")
print(x)
x1=a.get("twoo",123)
print(x1)
print(a)


#setdefault
a={"one":1,"two":2,"three":3}
x=a.setdefault("three",5)
print(x)
print(a)

a={1:1,2:2}
b={3:3,4:4}
a.update(b)
print(a)
a.update({5:5})
print(a)


a={1:1,2:2}
b=a.copy()
print(a[0])
print(b)



d={"fruit":"apple","veg":"onion","no":1,"age":23,"gender":"male"}
print(d)
for i in d:
    print(i)
for i,j in d.items():
    print(i,j)

for i in d.values():
    print(i)
    print([i])
    print({i})
    

for i in d.items():
    print(i)
    print([i])
    print({i})


for i in d.keys():
    print(i)
    print([i])
    print({i})

d={"details":{"fruit":"apple","veg":"onion","no":1,"age":23,"gender":"male","games":["crricket","volly","foot"]},"values":{"name2":"grill","value":"val1"}}
print(d)
for i in d:
    print (d)
 

fam={"child11":{"name":"yoki","age":23,"gender":"male"},"child2":{"name":"muthu","age":23,"gender":"male"},"child3":{"name":"mama","age":23,"gender":"male"}}
fam["child4"]={"name":"somu","age":24}
fam["child2"]["age"]=50
l={}
for i in fam.keys():
    print(i,end=" :")
    l.update(i)
    for j,k in fam[i].items():
        print(j,k,end=" ")
        
    print()    

print(l)


fam={"child11":{"name":"yoki","age":23,"gender":"male"},"child2":{"name":"muthu","age":23,"gender":"male"},"child3":{"name":"mama","age":23,"gender":"male"}}
fam["child4"]={"name":"somu","age":24}
fam["child2"]["age"]=50
l={}
for i in fam:
    for j in fam[i]:
        l[f'{i}:{j}']=fam[i][j]

print(l)        
        
a={"emploee":{"id":1,"name":"yoki","age":23},
   "detail":{"salary":2000000},
   "detail1":{"company":"google"}}
b={"employee2":{"id":2,"name":"muthu","age":23},
   "detail":{"salary":20000001,"sports":"fit"},
   "detail2":{"company":"apple"}}
l={}
for i in a:
    for j in a[i]:
        l[f'{i}:{j}']=a[i][j]
l1={}
for i1 in b:
    for j1 in b[i1]:
        l1[f'{i1}:{j1}']=b[i1][j1]
l.update(l1)
print(l)
"""
a={"emploee":{"id":1,"name":"yoki","age":23},
   "detail":{"salary":2000000},
   "detail1":{"company":"google"}}
b={"employee2":{"id":2,"name":"muthu","age":23},
   "detail":{"salary":20000001,"sports":"fit"},
   "detail2":{"company":"apple"}}
l={}
a.update(b)
for i in  a:
    for j in a[i]:
        l[f'{i}:{j}']=a[i][j]

print(l)
