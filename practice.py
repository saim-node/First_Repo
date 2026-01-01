import copy

books = {
    "The Great Gatsby": 15.99,
    "To Kill a Mockingbird": 12.49,
    "1984": 10.99,
    "Pride and Prejudice": 9.99,
    "Moby Dick": 8.99
}


copy_of_book = copy.copy(books)


all_sum = 0
after_sold = 0
for k,v in books.items():
    print("Title:" , k , "Value:" ,v)
    all_sum  = all_sum + v
    
print("---------------------------------")
for k,v in books.items():
    if "1984" == k:
        print("book title:",k,"and price",v," that was sold")
        after_sold = all_sum - v


print("Before Sold Price :" ,all_sum)
print("After Sold Price :" ,after_sold)