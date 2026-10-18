#=========================== 421. FizzBuzz =================================================
# numbers=(1,2,3,4,5,6,15,17,13,45,90,16,20,91,30)

# for num in numbers:
#     if (num % 3 == 0) and (num % 5 == 0):
#         print("fizzbuzz")
#     elif num % 5 == 0:
#         print("buzz")
#     elif num % 3 == 0:
#         print("fizz")
#     else:
#         print(f"{num}")

#=======================1365. How many num are smaller than the current numbers================================
lst = [8,3,1,2,1]
result = []
for i in lst:
    c=0
    for j in lst:
        if j<i :
            c+=1
    result.append(c)
print(result)