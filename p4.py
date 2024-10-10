#Lela-Parks
#Oct-08-2024


name = input('What is your name?')
name1 = "Lela"
name2 = "Ben"

if name == name1:
    print('Hello,' + name + "!")
elif name == name2:
    print('Hello,' + name + "!")
else: 
    print("you aren't welcomed here")
#Check if th user imput is name1


#Program will ask what the users name is while the 
#Print will greet that user only when they type their name in
#Guest who are not recorded are not welcomed

pi = 3.14159
# Prompt the user for the radius
radius = float(input("Enter the radius of the circle: "))

# Compute the area of the circle
area = pi * (radius ** 2)

# Print a message with the result
print(f"The area of the circle with radius {radius} is {area:.2f}")

# Import math Library
import math

# Print the value of pi
print (math.pi)
#Code is able to return the value of pi

# Prompt the user for the number of miles driven and gallons used
miles_driven = float(input("Please enter the number of miles driven: "))
gallons_used = float(input("Please enter the number of gallons used: "))

# Check if gallons used is not zero to avoid division by zero
if gallons_used <= 0:
    print("Gallons used must be greater than zero.")
else:
    # Calculate MPG
    mpg = miles_driven / gallons_used

    # Print the result
    print(f"The car's fuel efficiency is: {mpg:.2f} miles per gallon.")

#The program is supposed to help drivers calculate how efficently their vehicle is using fuel
#Assisting them to monitot their fuel consuption and costs