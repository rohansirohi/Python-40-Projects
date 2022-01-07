#welcome message
print("Welcome to the Temperature Conversion Program")
#input
temp_Fah = float(input("What is the given temperature in degrees Fahrenheit:"))
#formulae
temp_celsius = round(((temp_Fah - 32) * (5/9)),4)
temp_kelvin = round(((temp_Fah - 32) * (5/9) + 273.15),4)
#print in tabular format
print("\nDegrees Fahrenheit:\t" + str(temp_Fah))
print("Degrees Celsius:\t" + str(temp_celsius))
print("Degrees Kelvin:\t\t" + str(temp_kelvin))