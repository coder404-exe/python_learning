items = ["apple", "banana", "orange", "apple", "mango"]

is_unique=set()
for item in items:
    if item in is_unique:
        print("Dublicate :",item)
        break
    is_unique.add(item)