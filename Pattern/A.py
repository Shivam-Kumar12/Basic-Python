for row in range(7):
    for col in range(5):
        if (row==0 or row==2) or ((col==0 or col==4)and row==1 )or ((col==0 or col==4)and row==3) or ((col==0 or col==4)and row==4):
            print("*",end=" ")
        else:
            print(end="  ")
    print()