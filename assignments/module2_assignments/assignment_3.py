# Define a tuple containing mixed data types, unpack its values into separate variables, 
# and compare them with another tuple using comparison operators. 
# Then, explain in code comments the main difference between lists and tuples in Python.


t1=("apple",1,3.0)

# "tuple unpacking"
a,b,c=t1
print(f"a={a}, b={b}, c={c}")

#tuple comparison
t2=("apple",23,4)

print("t1==t2" ,t1==t2) 
print("t1>t2" ,t1>t2) 
print("t1<t2" ,t1<t2) 

# the main difference of list and tuple is that a list is mutable but a tuple is immutable