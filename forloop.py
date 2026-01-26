# i=0

# for i in range(1,1001):
#     print(i)

# a=[1,3,5,2,4,'a',8,6]    

# for i in a:
#     print(i)

# for j in a:
#     if type(j)==type("bbbb"):
#         # break
       
#         continue
#     else:
#         print(j)


a=[20,25,10,36,45,21]

result=[]

for i in a:
    if i%2!=0 :
        result.append(i)
    
# print(result)

result_new=[i**2  if i%2==0 else i for i in a]
print(result_new)