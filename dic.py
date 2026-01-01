dic = {"a":"Apple", "b":"Banana", "c":"Cat"}


# 1nd element using key 
# print("dic is ", list(dic.keys())[0])
# print("dic is ", list(dic.values())[0])

# #  upadate dic one value from dic 2

# dic2 = {"a":"Avocado", "d":"Dog"}
# dic.update(dic2)
# print("Updated dic is ", dic)

# print("Length of dic is ", len(dic))

# dic.update({"e":"Elephant"})
# print("Updated dic is ", dic)

# dic.update(E="Eagle")
# print("Updated dic is ", dic)


# remove element
dic.pop("b")
print("After pop dic is ", dic)

dic.popitem()
print("After popitem dic is ", dic)


mi = {"x":100, "y":200, "z":300}
key = "y"

if key in mi.keys():
    print(f"{key} is present in mi")
    mi.update({key:600})
    print("After update mi is ", mi)
else:
    print(f"{key} is not present in mi")


studnets = {
    "name":"Ali",
    "age":20,
    "city":"Lahore"
}
# setdefault() — Insert if missing
studnets.setdefault("country", "Pakistan")
# If exists → no change
# If not → adds key

print("After setdefault studnets is ", studnets)





# Q1

# Create a dictionary:

person = {"name": "Sara", "age": 22}


# Do this:
# Print name using get()
# Add "city": "Lahore"
# Change age to 23
# Loop and print:

print("The person name is ",person.get("name"))
person["city"] = "Lahore"
print(person)
person["age"] = 23

for k,v in person.items():
    print(k,"->",v)


# Q1 (Easy)

# Create this dictionary:

person1 = {
    "name": "Ahmed",
    "address": {
        "city": "Karachi",
        "zip": 12345
    }
}


# Print:
# City is Karachi
print("city ", "is",person1.get("address").get("city"))

# Q2 (Medium)

# Using the same dictionary:
# Change city to "Lahore"
# Add "country": "Pakistan" inside address
# Print full dictionary

person1.get("address")["city"] ="Lahore" 
person1.get("address").update({"country" : "Pakistan"})

print(person1)




# Q3 (Important Logic)

# Create:
students1 = {
    "Ali": {"math": 80, "english": 70},
    "Sara": {"math": 90, "english": 85}
}


# Loop and print like:
# Ali
#  math -> 80
#  english -> 70
# Sara
#  math -> 90
#  english -> 85



for name, marks in students1.items():
    print(name)
    for subject, score in marks.items():
        print(" ", subject, "->", score)
