name = input("Enter your name: ") 
age = int(input("Enter your age: "))  
counrty = input("Enter your countre of birth: ")  
popular = input("What are you known for?")

user_info = {
    "What is the user's name?": name,
    "What is the user's age?": age,
    "What is the user's counrty of birth?": counrty
    "What is the user known for?": popular
}

print("\nUser Information:")
for key, value in user_info.items():
    print(f"{key.capitalize()}: {value}")
