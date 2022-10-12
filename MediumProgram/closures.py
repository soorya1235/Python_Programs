def outer():
    msg = "ello world"
    def inner():
        print(msg)
    return inner


a = outer()
a()
a()
a()
