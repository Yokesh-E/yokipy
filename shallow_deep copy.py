#shallow copy & deep copy
"""
#shallow copy
import copy
a=[[1,2,3,4],[5,6,7,8]]# its works only nested list
b=copy.copy(a)
a[0][1]=12
print(a)
print(b)

#deepcopy

c=[[1,2,3,4],[5,6,7,8]]# its works only nested list
d=copy.deepcopy(c)
c[0][1]=13
print(c)
print(d)
"""
import copy
a={"stud1":{"name":"yoki","age":23},"stud2":{"name":"yki","age":21}}
b=copy.copy(a)#its works only nested dict
a["stud1"]["name"]="laki"
print(a)
print(b)
