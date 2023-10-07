# prompt the user for inputs
first_name = input("Enter your first name: ")
last_name = input("Enter yiur last name: ")
email_address = input("Enter your email address: ")
phone_number = input("Enter your phone number: ")
location = input("Enter your location: ")

# creating a list to store the outputs
user_info = [first_name, last_name, email_address, phone_number, location]

# print the list of outputs
print("user information:")
for item in user_info:
    print(item)