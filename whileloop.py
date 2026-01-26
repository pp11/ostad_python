#sum of all elements in the list
# a=[1,2,3,4,5,6]

# sum=0

# i=0
# l=len(a)
# print(l)
# while i<l:
#     sum=sum+a[i]
#     i+=1
# print(sum)

a=[-10,2,19,-3,-5]

# a[1]=0
print(a)
n=len(a)
i=0
while i<n:    
    if a[i]<0:
        a[i]=0
    i+=1
print(a)

