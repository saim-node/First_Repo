def dimond(n):

    if n % 2 == 0:
        print("Please Give an ood number")
        return

    mid = n // 2 #
    for i in range(mid+1) :
        print(" " * (mid-i) + "*" *(2*i + 1))
    
   
    for i in range(mid-1,-1,-1) : # it runs two steps
        print(" " * (mid-i) + "*" *(2*i + 1))
    
        


print("Welcome to diamond world :")

user_input = int(input("Enter an odd number : "))
dimond(user_input)
