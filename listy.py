# data = list(map(int,input("enter : ").strip()))
# print(data)

# o = [10, "20", "30"] 

# ======================================= Lamda Function =======================================

def add_five(x):
    return x + 5

a = lambda x:x+5
print(a(10))

print((lambda x:x+5)(10))

# ======================================= End ==================================================

# ======================================= Split Function =======================================

# ⚠️ split() does NOT change the original string
# Strings are immutable

data = "10 20 30 40 50"
print(data.split())

# ======================================= End ==================================================

# ====================================== Append Function =======================================
data = [10, 20, 30]
data.append(40)
print(data)

international_cars = ["Bmw","G-wagon","Bently"]
local_cars = ["Tz","Mark X","Grande"]

my_cars_collection = []

for i in international_cars:
    my_cars_collection.append(i)

for i in local_cars:
    my_cars_collection.append(i)


print(my_cars_collection)
# ======================================= End ==================================================


# ======================================= Extend  =================================================

# it takes a list and add/put in other list one by one

international_cars = ["Bmw","G-wagon","Bently"]
local_cars = ["Tz","Mark X","Grande"]

my_cars_collection = []

my_cars_collection.extend(international_cars)
my_cars_collection.extend(local_cars)

my_cars_collection.reverse() 
print(my_cars_collection)

# list.remove(value)
a= [1,2,3]
a.remove(2)
print(a)


# pop() is a list method.

# It:
# removes an item by index
# returns the removed item

nums = [10, 20, 30]
x = nums.pop()

print(x) # 30 if no index given then it gives the last item
print(nums) # [10,20]


# Method	    Removes by	    Returns value?
# --------------------------------------------
# pop	        index	            ✅ Yes
# remove	    value	            ❌ No
# --------------------------------------------





square_list = []

for i in range(101):
    if i % 2  == 0:
        square_list.append(i*i)
    
print(square_list)