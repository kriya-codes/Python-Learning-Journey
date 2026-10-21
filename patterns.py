
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

#=======================================Pattern 5===========================================
def full_pyramid(n):
    #Star
    for i in range(1, n+1):
        for j in range(1, n-i+1):
            print(" ", end="")
        for k in range(1, 2*i):
            print("*", end="")
        print()

#=======================================Pattern 6===========================================
def reversed_pyramid(n):
    #Star
    for i in range(n, 0, -1):
        for j in range(1, n-i+1):
            print(" ", end="")
        for k in range(1, 2*i):
            print("*", end="")
        print()

#=======================================Pattern 7===========================================
def diamond(n):
    #Star
    for i in range(1, n+1):
        for j in range(1, n-i+1):
            print(" ", end="")
        for k in range(1, 2*i):
            print("*", end="")
        print()
    for i in range(n, 0, -1):
        for j in range(1, n-i+1):
            print(" ", end="")
        for k in range(1, 2*i):
            print("*", end="")
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

print("\nPattern 5: Full Pyramid")
full_pyramid(n)

print("\nPattern 6: Reversed Pyramid")
reversed_pyramid(n)

print("\nPattern 7: Diamond")
diamond(n)