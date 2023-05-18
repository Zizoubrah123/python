def countdown(n):
    return list(range(n, -1, -1))

print(countdown(5))



def print_and_return(z):
    print(0)
    return (1)

print(print_and_return([1,2]))


def first_plus_length(a):
    return a[0] + len(a)

print(first_plus_length([1,2,3,4,5]))


def new_list (aze):
    sum = aze
    if len(aze) > 2:
        for i in range(len(aze)):
            print(aze[2])
            return (aze[::2])

print(new_list([5,2,3,2,1,4]))


def integers (size, value):
    return [value] * size

az = integers (5,1)
print (az)