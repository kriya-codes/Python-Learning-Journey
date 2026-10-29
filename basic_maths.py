def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact) 

#=======================================Main Program=========================================
n = int(input("Enter a number: "))
print("Factorial of",n,":")
factorial(n)