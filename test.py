
def countdown(n):
    return list(range(n, -1, -1))

countdown_list = countdown(5)
print(countdown_list)


def print_and_return(z):
    print(a[0])
    return (a[1])

a = [1,2]
print_return = print_and_return(a)


def plus_list(a):
    return a[0] + len(a)

a = [1,2,3,4,5]
b = plus_list(a)
print (b)

def new_list (aze):
    sum = aze
    if len(aze) > 2:
        for i in range(len(aze)):
            print(aze[2])
            return (aze[::-2])

aze = [1,2,3,4,5]
ab = new_list(aze)
print(ab)


def integers (size, value):
    return [value] * size

az = integers (5,1)
print (az)