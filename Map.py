# map method in python


def add_one(x):
    return x + 1

nums = [1, 2, 3]
result = map(add_one, nums)
# print(list(result))


# practical examples
i = [2, 4, 6]

def mul(x):
    return x * 3

r= map(mul,i)

print(list(r))
