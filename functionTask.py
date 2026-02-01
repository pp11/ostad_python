# # no input, no return
# def myFunction():
#     a=12
#     b=7
#     print(a+b)

# myFunction()

# # input , no return

# def add(a,b):
#     sum=a+b
#     print("the result is",sum)

# add(2,3)

# # input ,return

# def multiply(a,b):
#     return a*b

# result=multiply(5,10)
# print(result)

# #no input, return

# def hello():
#     return "hello"

# greet=hello()
# print(greet)

# #Multiple arguments
# def addition(*args):
#     result=sum(args)
#     return result

# r=addition(1,5,3,6)
# print(r)

#keyword argument
# def test(f_name, l_name, age):
#     print(f"I am {f_name} {l_name}. I am {age} years old.")

# test(age=35, f_name='priyanka',l_name='podder')

#arbitary arguments

def test(**data):
    print(data)
    print(f'I am {data['f_name']} {data['l_name']}. My age is {data['age']}')

test(age=35, f_name='priyanka',l_name='podder')

def my_name(f_name, l_name="podder"):
    print(f'my name is {f_name} {l_name}')

my_name("priyanka")

def my_name2(f_name, l_name="podder"):
    pass

my_name2("priyanka")