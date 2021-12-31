
print("Welcome to the first project")

# Output the name of user
name = input("What is your name: ")
print("Hello",name.title())

# Goal of the project
print("I will count the number of times that a specific letter occurs in a message")
message = input("Please enter a message: ")
letter = input("Which letter would you like to count the occurance of: ")

#Convert to lower case
message = message.lower()
letter = letter.lower()

#Get count and display result
letter_count = message.count(letter)
print("\n" + name + ", your message has " + str(letter_count) + " " + letter + " in it.")
