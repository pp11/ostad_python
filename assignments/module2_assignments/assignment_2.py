
# Create a function that accepts two sets as parameters 
# and returns their union, intersection, and difference. 
# Use keyword arguments with default parameter values so the function can work even 
# if one of the sets is not provided by the user. 
# Display the results clearly.

def set_operation(s1, s2={1,5}):
    union_result=s1.union(s2)
    intersect_result=s1.intersection(s2)
    diff_result=s1.difference(s2)
    print(f"union result is : {union_result}")
    print(f"intersection result is : {intersect_result}")
    print(f"difference result is : {diff_result}")


set_operation({1,3,2,5,10},{1,10,20,30})

set_operation({1,3,2,5,10})