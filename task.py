# ==================== classword ========= 

names = []

print("Welcome")

user_input = input("Do you Want to Add a name  type(y/n) ").strip()
 

if user_input == "y":
    while True:
        u_input = input("Enter  a new name or type done to exit ")
        if u_input == "done":
            break
        elif u_input in names:
            names.remove(u_input)
        else:
            names.append(u_input)
            
print(names)