# a=[1,3,6,'ab','bh']

# print(a)
# a.append([4,5,6])
# print(a)


# s = "hello"
# b=list(s)

# print(b)

# for i in b:
#     print(i, end="")

mylist = ['apple', 'banana', 'cherry', 'orange', 'kiwi']

# print(mylist[1:2])

# mylist.remove('cherry')
# mylist.append('apple')
# mylist.remove('apple')
# print(mylist)


t= ('apple', 'banana', 'cherry','apple', 'orange', 'kiwi','apple')

t_new=tuple(reversed(t))

print(t)
print(t_new)

print(t.index('banana'))
print(t.count('apple'))



l=[2,4,1,3,6,59,12]

print(sorted(l))