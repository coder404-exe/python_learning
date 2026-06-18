# Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).
distance=int(input("How much distacne : "))

if distance<3 :
    transportation="walk"
elif distance>=3 and distance<=15:
    transportation="bike"
elif distance>15:
    transportation="car"

print(transportation)