def operation_1():
    print("Operation 1: Calculate the area of a circle")
    radius = float(input("Enter the radius: "))
    area = 3.14159 * (radius ** 2)
    print(f"Area of the circle: {area}")

def operation_2():
    print("Operation 2: Calculate the velocity of an object")
    distance = float(input("Enter the distance (m): "))
    time = float(input("Enter the time (s): "))
    velocity = distance / time
    print(f"Velocity: {velocity} m/s")

def operation_3():
    print("Operation 3: Calculate the force")
    mass = float(input("Enter the mass (kg): "))
    acceleration = float(input("Enter the acceleration (m/s²): "))
    force = mass * acceleration
    print(f"Force: {force} N")

def operation_4():
    print("Operation 4: Calculate the quadratic roots")
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    discriminant = b ** 2 - 4 * a * c
    if discriminant >= 0:
        root1 = (-b + discriminant ** 0.5) / (2 * a)
        root2 = (-b - discriminant ** 0.5) / (2 * a)
        print(f"Roots: {root1}, {root2}")
    else:
        print("The equation has complex roots.")

def operation_5():
    print("Operation 5: Calculate the kinetic energy")
    mass = float(input("Enter the mass (kg): "))
    velocity = float(input("Enter the velocity (m/s): "))
    kinetic_energy = 0.5 * mass * (velocity ** 2)
    print(f"Kinetic Energy: {kinetic_energy} J")

# Mapping input to the corresponding function
operations = {
    'a': operation_1,
    'b': operation_2,
    'c': operation_3,
    'd': operation_4,
    'e': operation_5
}

# Get user input
user_input = input("Enter a letter (a-e) to select an operation: ").lower()

# Call the corresponding function
if user_input in operations:
    operations[user_input]()
else:
    print("Invalid input. Please enter a letter from 'a' to 'e'.")