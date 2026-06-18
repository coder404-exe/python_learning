# Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).
weather=input("How is the weather : ")

if(weather.lower()=='sunny'): 
    print("Go for a walk")
elif weather.lower()=="rainy" :
    print("Read a book")
elif weather.lower()== "snowy":
    print("Build a snowman")