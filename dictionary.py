a = {
    "id": 101,
    "name": "Rahim",
    "age": 20,
    "passed": True
}

print("---key----")

for i in a:
    print('key' , i)

print("---value----")

for i in a.values():
    print('values' , i)

print("------key value------")

print(a.keys(), a.values())

print("------key value pair------")

for k ,v in a.items():
    print(f"key : {k}, values: {v}")

a=[1,2,3,4]
b = ["A", "B", "C",'d']  

c=dict(zip(a,b))
print(c)

print("--------------------")

num=list(range(0,11))

result={i : "even" if i%2==0 else "odd" for i in num }

print(result)
