

def m1():
    print("Hello World")
    l = [1, 45, 25, 16, 34, 19, 83]
    for i in l:
        l[l.index(i)] = i*i
    print("squared list- ",l)

