numbers=(1,2,3,4,5,6,15,17,13,45,90,16,20,91,30)

for num in numbers:
    if (num % 3 == 0) and (num % 5 == 0):
        print("fizzbuzz")
    elif num % 5 == 0:
        print("buzz")
    elif num % 3 == 0:
        print("fizz")
    else:
        print(f"{num}")
