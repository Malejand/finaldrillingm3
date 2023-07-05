# def a():
#     return 5
#     return 10


# print(a())

# def a():
#     print(5)


# x = a()  # None
# print(x)

# def a(a, b):
#     return str(a) + str(b)  # Al ser strings no se suman, se concatenan


# print(a(2, 5))


def factorial(x):
    if x <= 1:
        return 1
    else:
        return (x * factorial(x-1))


print(factorial(0))
print(factorial(5))
print(factorial(-5))
