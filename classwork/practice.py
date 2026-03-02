# print("hello worldpriyanka
# 
# ") #cd

"""
print("hello world")
print("hello world")
print("hello world")
"""

# fname=input("enter first name ")
# lname=input("enter last name" )

# print(fname,lname)


# a, b= 2 , 2j

# print(complex(a)+b)

s1={1,2,3,5,1,6}

s2={True, 1,0 }

s2.add(66)
s2.update(s1)


# s2.remove(6666)
s2.discard(6666)
s2.pop()
print(s2)



a={1,5,66,2,3,7}
b={2,4,6,8}

# c=a.union(b)
# c=a.intersection(b)
c=a.difference(b)
print(c)



thistuple=("apple",'banana','cherry','apple')

# thistuple.add("oraNge")

thiset=set(thistuple)
print(thistuple)



thiset.add("orange")

thistuple=tuple(thiset)

print(thiset)

print(thistuple)

