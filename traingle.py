import math
#welcome message
print("Welcome to the Right Traingle Solver App")
#input data
side_a = float(input("What is the first leg of the traingle:"))
side_b = float(input("What is the second leg of the traingle:"))
#formula
side_c = round((math.sqrt(side_a**2 + side_b**2)),3)
area = round((0.5*side_a*side_b),3)
#output
print("Hypotenuse is: ", str(side_c))
print("Area is:", str(area))