# Ask for user's name using input, save to name variable, then print name
# Print "Git is awesome!" string
print("Git is awesome!")
response = input("Do you agree? ")
print(response)

if response == "no":
    print("Fair enough.")
elif response == "yes":
    print("Great stuff!")
else:
    print("User error. Must respond 'yes' or 'no'.")