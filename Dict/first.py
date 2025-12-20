# Q1
# Create a dictionary named student with:
# name
# age
# marks
# Then:
# print the dictionary
# remove age using pop() and print the removed value

dic = {
    "name": "John",
    "age": 21,
    "marks": 85
}
r = dic.pop("age")
print(r)


# Q2
# Create a dictionary of 3 fruits with prices.
# Delete one fruit using del and print the dictionary.

dic = {
    "apple":400,
    "orange":300,
    "mango":1000,
}

del dic["apple"]
print(dic)



# Q3
# Given:
data = {"a": 10, "b": 20, "c": 30}
# Write code to:
# remove "b" using pop()
# store the removed value
# print the value and updated dictionary

x  = data.pop('b')
print(x)


# Q4
# Write a program that:
# takes a key name from the user
# safely removes it from a dictionary using pop()
# if key doesn’t exist, print "Key not found"

# print(data)
# user_input = input("Enter a Key You Want to Remove").strip()

# if user_input in data:
#     data.pop(user_input)
#     print("Key Found and Delted Successfully")
# else:
#     print("Key Not Found")
# print(data)


# Q5
# Given:
inventory = {
    "apple": 10,
    "banana": 5,
    "orange": 8
}
# Write code to:
# remove items with quantity less than 6
# print the updated dictionary

for k, v in list(inventory.items()):
    if v < 6:
        inventory.pop(k)

print(inventory)


# Write a function remove_key(d, key) that:
# removes the key using del
# handles the case where key does not exist (no crash)
# returns the updated dictionary
    

def remove_key(d, key):
    if key in d:
        del d[key]
    return d



Dict = remove_key({"a":10,"b":2},"b")
print(Dict)



# Dictonray deep methods

# 1️⃣ get() — SAFE access (No crash)

# 2️⃣ update() — Add or Change multiple items

student = {"name": "Ali", "age": 20}

student.update({"age": 21, "grade": "A"})
print(student)


# 3️⃣ setdefault() — Get OR Insert
# If key exists → returns value
# 👉 If not → adds it

d = {"a": 1}

d.setdefault("a", 100)
d.setdefault("b", 200)

print(d)

d = {"x": 10, "y": 20}

print(d.keys())    # dict_keys(['x', 'y'])
print(d.values())  # dict_values([10, 20])
print(d.items())   # dict_items([('x', 10), ('y', 20)])
# ======================================================================

data = {"name": "Sara", "age": 22}
# Print city using get() (no error)
# Use setdefault() to add "city": "Lahore"
# Print dictionary

data.get("city")

data.setdefault("city", "Lahore")
print(data)


dict1 = {"name": "Sara", "age": 22}
dict2 = {"city": "Lahore", "country": "Pakistan"}

dict1.update(dict2)

print(dict1)



marks = {"math": 80, "english": 75, "science": 90}
for k,v in marks.items():
    print(f'{k} -> {v}')

# Q4 (Important Logic)

# Given:
d = {}
# Write code so that:
# if key "count" exists → increase value by 1
# if not → set it to 1
#(Hint: setdefault() OR get())

d["count"] = d.get("count", 0) + 1



# ===========================================
# d.copy()    → returns a shallow copy of dictionary d.
# d.pop(key)  → removes and returns the value for the given key.
# d.popitem() → removes and returns the last inserted (key, value) pair.
# d.clear()   → removes all items from the dictionary.
# dict.fromkeys(keys, value) → creates a new dictionary with given keys and a common value.


# Example of fromkeys():

keys = ['a', 'b', 'c']
d = dict.fromkeys(keys, 0)
print(d)


# Output:
{'a': 0, 'b': 0, 'c': 0}
