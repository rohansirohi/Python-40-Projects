#welcome message
print("Welcome to the miles per hour conversation app")
#get the input
miles  = float(input("What is your speed in miles per hour: "))
#convert into meter per second
meter = round((miles / 2.237),2)
#print the answer
print("Your speed in meteres per second is", meter)