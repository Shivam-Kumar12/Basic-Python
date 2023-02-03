for i in range(1,8):
    for j in range(1,27):
        if ((i == 2 or i == 3) and (j == 1 or j == 8 or j == 17 or j == 24)  ):
            print("*",end=" ")

        elif ((i == 5 or i == 6) and (j == 5 or j == 12 or j == 17 or j == 24)):
            print("*",end=" ")

        elif ((i == 4) and (j == 2 or j == 3 or j == 4 or j == 9 or j == 10 or j == 11 or j == 17 or j == 24)):
            print("*",end=" ")

        elif ((i == 1) and (j == 2 or j == 3 or j == 4 or j == 9 or j == 10 or j == 11 or j == 15 or j == 16 or j == 17 or j == 18 or j == 19 or j == 22 or j == 23 or j == 24 or j == 25 or j == 26)):
            print("*",end=" ")

        elif ((i == 7) and (j == 2 or j == 3 or j == 4 or j == 9 or j == 10 or j == 11 or j == 17 or j == 15 or j == 16 or j == 24 or j == 18 or j == 19)):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
