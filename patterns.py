
#=======================================Pattern 1===========================================
def square_star(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print("*", end=" ")
        print()


#=======================================Pattern 2===========================================
def right_angle(n):
    # Star
    for i in range(1, n+1):
        for j in range(1, i+1):
            print("*", end=" ")
        print()

    # Number
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()


#=======================================Pattern 3===========================================
def repeated_number(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(i, end=" ")
        print()


#=======================================Pattern 4===========================================
def inverted_triangle(n):
    # Star
    for i in range(1, n+1):
        for j in range(1, n-i+2):
            print("*", end=" ")
        print()

    # Number
    for i in range(1, n+1):
        for j in range(1, n-i+2):
            print(j, end=" ")
        print()


#=======================================Main Program=========================================
n = int(input("Enter a number: "))

print("\nPattern 1: Square Star")
square_star(n)

print("\nPattern 2: Right Angle")
right_angle(n)

print("\nPattern 3: Repeated Number")
repeated_number(n)

print("\nPattern 4: Inverted Triangle")
inverted_triangle(n)
