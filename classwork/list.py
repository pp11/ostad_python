# snacks=["soda",'cake','apple','cookies']


# snacks.append('chips') #last e add hobe
# print(snacks)


# snacks.remove("soda")
# print(snacks)

# snacks.sort()
# print(snacks)

snacks=['cake','apple',"soda",'cookies','sprite']

snacks[2]='juice' #replace hobe

print(snacks)
snacks.append('chips') #last e add hobe
snacks.insert(2,'banana') #specific jaigai add hobe

snacks.remove("sprite")

del snacks[0]  #index dhore value delete hobe

print(snacks)

print("first item", snacks[0])
print("last item", snacks[-1])
#or
print("last item", snacks[len(snacks)-1])

last_item=snacks.pop()
print(last_item)
print(snacks)

snacks.clear()
print(snacks)




# color=["red","blue"]

# print(color[0])

# color[1]="yellow"

# # Add "purple" to the end
# color.append("purple")

# # Remove "red"
# color.remove("red")

# # Print the list

# print(color)