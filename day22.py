
# while True:
#     num=int(input("Enter the num : "))
#     limit=int(input("enter the limit for multiplication: "))
#     print(f"multiplication table of {num}")

#     for  i in range(1,limit+1):
#         print(f"{num} X {i}= {num*i}


numbers=int(input("Enter the number u wanna  multiplication from:"))
numbers_to=int(input("Enter the number u wanna  multiplication to:"))
limits=int(input("Enter the limits: "))
for i in range(numbers,numbers_to+1):
    print(f"multiplication table of {i}")

    for  j in range(1,limits+1):
        print(f"{i} X {j}= {numbers*j}")

