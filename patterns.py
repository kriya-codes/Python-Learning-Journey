#=======================================Pattern 1===========================================
n = int(input("Enter a number:"))
# square_star pattern
for i in range(1, n+1):
    for j in range(1, n+1):
        print("*" , end=" ")
    print()

#=======================================Pattern 2===========================================
# right_angle star pattern
for i in range(1, n+1):
    for j in range(1, i+1):
            print("*" , end=" ")
    print()
# right_angle number pattern
for i in range(1, n+1):
    for j in range(1, i+1):
            print(j , end=" ")
    print()

#=======================================Pattern 3===========================================
# repeated_number pattern
for i in range(1, n+1):
    for j in range(1, i+1):
            print(i , end=" ")
    print()

#=======================================Pattern 4 ===========================================
# inverted_star pattern
for i in range(1, n+1):
    for j in range(1, n-i+1):
            print("*" , end=" ")
    print()

# inverted_number pattern
for i in range(1, n+1):
    for j in range(1, n-i+1):
            print(j , end=" ")
    print()