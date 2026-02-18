# dict={"name" : "priyanka",
#       "age" : 35,
#       "fav_color":"purple"}

# # print(f"name {dist["name"]}, age : {dist["age"]}")

# print("name {} , age {}".format(dict["name"], dict["age"] ))

# # dict.pop("age")

# dict["phone"]="01777036369"
# # del dict["phone"]

# print(dict)


# for k,v in dict.items():
#     print(k, v)

# for k in dict.keys():
#     print(k)

# for i in dict.values():
#     print(i)


dict_details={
 "stu1":{"name" : "priyanka","age" : 35,  "fav_color":"purple"}, 
 "stu2":{"name" : "pp","age" : 36,  "fav_color":"pink"}
}

print(dict_details["stu1"]["name"])

for k ,v in dict_details.items():
    print(f"{k}, {v["name"]} is {v["age"]} and her favourite color is {v["fav_color"]}")


    