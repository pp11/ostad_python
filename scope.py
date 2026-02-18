n="global"

def outer():
    n="enclosing"
    def inner():
        # global n
        nonlocal n
        n="Local"
        print(n)

    inner()
    print(n)

outer()
print(n)