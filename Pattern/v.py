for row in range(7):
    for col in range(11):
        if(row==0 and (col==0 or col==10)) or (row==1 and (col==1 or col==9)) or (row==2 and (col==2 or col==8)) or (row==3 and (col==3 or col==7)) or (row==4 and (col==4 or col==6)) or (row==5 and col==5): 
            print("*",end="")
        else:
            print(end=" ")
    print()