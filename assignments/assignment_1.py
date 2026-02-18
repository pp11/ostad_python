
# Assignment on module 2
# 1. Write a Python program that takes a list of numbers as input, 
# removes duplicates using a suitable list method, and returns a dictionary 
# containing the original list, the unique values, and their count. 
# Use a function with parameters and a return statement to perform this task.


def list_func(num):
    unique_values=set(num)
    num_count=len(num)

    dict={
        "orginial_list":num,
        "unique_values" : unique_values,
        "num_count" : num_count
    }
    return dict


print(list_func([8,1,6,2,6,4,7,3]))
