for row in range(7):
    for col in range(5):
        if (row==0 or row==5) or (col==2 and (row>0 and row<5)): 
            print("*",end="")
        else:
            print(end=" ")
    print()