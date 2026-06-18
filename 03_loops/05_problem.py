input_str=input("Enter String: ")

for char in input_str:
    char_count=input_str.count(char)
    if char_count==1:
        print(char) 
        break
