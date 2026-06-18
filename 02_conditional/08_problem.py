# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).
password=input("Enter password: ")
pass_length=len(password)

if pass_length<6 :
    pass_strength="weak"
elif pass_length>=6 and pass_length<10:
    pass_strength="Medium"
elif pass_length>=10:
    pass_strength="Strong"

print(pass_strength)                                                                                                                                                    