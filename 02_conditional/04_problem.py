# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)
color=input('Enter color of banana : ')

if(color.lower()=="green"): 
    print("Unripe")
elif(color.lower()=="yellow"):
    print("Ripe")
elif(color.lower()=="brown"):
    print("Overripe")