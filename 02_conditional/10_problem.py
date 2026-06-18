# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).
pet_type=input("What type of pet : ")
pet_age=int(input("Enter age of pet : "))

if pet_type.lower()=="dog":
    if pet_age<2 : food="Puppy Food"
    elif pet_age>=2 and pet_age<7 : food="Adult Dog Food"
    else: food="Senior Dog Food"
elif pet_type.lower()=="cat":
    if pet_age<1:food="Kitten Food"
    elif pet_age>=1 and pet_age<5: food="Adult Cat Food"
    else: food="Senoir Cat Food"

print(food)