#=======================================Pattern 1===========================================
n = int(input("Enter a number:"))
for i in range(1, n+1):
    for j in range(1, n+1):
        print("*" , end=" ")
    print()

#=======================================Pattern 2===========================================
n = int(input("Enter a number:"))
# star pattern
for i in range(1, n+1):
    for j in range(1, i+1):
            print("*" , end=" ")
    print()
# number pattern
for i in range(1, n+1):
    for j in range(1, i+1):
            print(j , end=" ")
    print()