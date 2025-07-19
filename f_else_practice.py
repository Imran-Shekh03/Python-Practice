age = int(input("Enter the age of the persion : "))

if age < 13:
    print("The person is a child")
elif age >= 13 and age <= 19:
    print("The person is an Teenager ")
elif age >= 20 and age <= 59:
    print("the person is an Adult ")
else :
    print("the person is a senior citizen")
