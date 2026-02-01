# # def square(x):
# #     print(x*x)

# # square(5)

# import functools


# square = lambda x: x*x
# add=lambda a,b:a+b

# print(square(5))

# print(add(2,3))

# # l=[1,3,4,6,5,9,10]

# check_even= lambda x : 'EVEN' if x%2==0 else "odd"
# print(check_even(5))

# #sorted list of tuple
# student = [("A",90), ("B",45),("C",60),("D",52)]

# sorted_student = sorted(student, key= lambda x :x[1])

# print(sorted_student)

# #sorting list
# l=[1,3,4,6,5,9,10]
# l.sort(key= lambda x:x)

# print(l)

# ##MAP
# result=list(map( lambda  x: x*x, l))
# print(result)


# even_l= list(filter( lambda x : x%2==0 ,l))
# print(even_l)


# addition_list= functools.reduce(lambda x, y:x+y , l)

# print(addition_list)


num=[1,2,3,5,6]

result=list(map(lambda x : x*2, num))

print(result)