# if __name__ == '__main__':
#     n = int(input("enter a number : "))
#     if n%2!=0:
#         print("Weird")
#     else:
#         if n>=2 and n<=5:
#             print("Not Weird")
#         elif n>=6 and n<=20:
#             print("Weird")
#         elif n>20:
#             print("Not Weird")


# def is_leap(year):
#     if year%4==0:        
#         if year%100==0:
#             if year%400==0:
#                 return bool(1)
#             else:
#                 return bool(0)
#         else:
#             return bool(1)
#     else:
#         return bool(False)
    
        
# year = int(input("please enter a year : "))\

# print(is_leap(year))

n = int(input())
for i in range(n+1):
    if i>0:
        print(i, end="")


    