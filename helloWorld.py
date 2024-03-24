# Ask for user's name using input, save to name variable, then print name
# Print "Git is awesome!" string
print("Git is awesome!")
response = input("Do you agree? ").lower()
print(response)

if response == "no":
    print("Fair enough.")
elif response == "yes":
    print("Great stuff!")
else:
    print("What you talkin' about, Willis?")