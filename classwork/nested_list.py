snacks=[
    ['cake','apple'],
    ["soda",'cookies'],
    ['sprite','coca-cola']
]

print(snacks)

j=0
for bag in snacks:
    
    
    j+=1 
    
    if j==2:
        # break
        continue
    print(f"{j} category")  
    for i in bag:  
        print(i)
       