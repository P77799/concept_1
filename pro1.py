# def tri():
#     line=int(input("Enter the num="))
#     for i in range(1,line+1):
#         for j in range(i):
#             print("*",end="")
#         print()

#     return line

# triangle=tri() 
# print(triangle)

def tri():
    line=int(input("Enter how many num of line do u want?"))
    for i in range(5,0,-1):
        for j in range(i):
            print("*" ,end=" ")
        print()
tri()

        