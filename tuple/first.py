# Q1
# Create a tuple of 5 numbers and print:
# the tuple
# its length
print("___________________")
first_tuple = (1,2,3,4,5)
print(first_tuple)
print(len(first_tuple))



# Q2
# Create a tuple with one element only and print its type.
print("___________________")
t = (1,)
print(type(t))

# Q3
# Write code to unpack this tuple:
t = ("Python", 3.12)
print("___________________")
a,b= t
print(a)
print(b)

# Q4
# Given:
t = (1, 2, 3, 2, 4)
# Write code to:
# print how many times 2 appears
# print the index of first 2
print("___________________")
print(t.count(2))
print(t.index(2))
print("___________________")
# contcatination

myt1=("sunday","saturday")
myt2=("monday","tuesday","wednesday","thursday","friday")
days_of_week =  myt2  + myt1 
print(days_of_week)

t = (1,2)
a,b = t

# Q5
# Write a function get_min_max() that:
# takes a tuple of numbers
# returns minimum and maximum values
# Example call:
print("___________________")
def get_min_max(a):
    return min(a) ,max(a)

print(get_min_max((10, 5, 20, 3)))

# Q6
# Write code to:
# convert a list into a tuple
# then convert it back to a list
print("___________________")
li = [1,2,3,4]
tuple_converstion = tuple(li)
back_to_list = list(li)
print(li)
print(tuple_converstion, "this is tuple with type ", type(tuple_converstion))
print(back_to_list, "this is tuple with type ", type(back_to_list))
print("___________________")


# Q7
# Given a tuple:
# Write code to add 5 inside the list without changing the tuple itself.
t = (1, [2, 3], 4) 

print(t[1].append(5))

# Q8 (Logic + Tuple)
# Write a program that:
# takes user input numbers separated by commas
# converts them into a tuple of integers
# Example input:

10,20,30
# inpt = input("user inpt : ").strip().split(",")
# print(inpt)
# li = []
# for i in inpt:
#     if i != "":
#         li.append(i)

# print(tuple(li))

li = [6,8,5,6,1,2]
print(li.index(1) ) 

# index(value,index_start,index_end)

li =[1,2,3,4,5]


count=0
for j in li:
    count+=1

for i in range(count):
    print(li[i])