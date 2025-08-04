print("-"*40)
print("------Area Calculation System------")
print("-"*40)

print("Please select a area type: ")
print("1. Area of Rectangle")
print("2. Area of circle")
print("2. Area of traingle")
print("2. Area of square")
print("-"*40)

choice = int(input("Enter your choice:"))
print("-"*40)

if choice == 1:
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    area = length*width
    print("area of rectangle:",area)

if choice == 2:
    r = float(input("Enter the radius of circle:"))
    area = 3.14159 * r * r
    print("area of circle:",area)

if choice == 3:
    base = float(input("Enter the base: "))
    height = float(input("Enter the height: "))
    area = 0.5 * base * height
    print("area of traingle:",area)

if choice == 4:
    side = float(input("Enter one side: "))
    area = side ** 2
    print("The area of square:",area)