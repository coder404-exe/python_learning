# Problem: Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).
year=int(input("Enter a year : "))


if year%400==0  or (year%100!=0 and year%4==0):
    print("It is a leap year")
else :
    print("It is not leap year")
