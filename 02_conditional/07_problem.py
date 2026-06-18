size = input("What size of coffee: ")
extra_shot = input("Want extra shot? (yes/no): ")

if extra_shot.lower() == "yes":
    print(size + " + Extra shot")
else:
    print(size)