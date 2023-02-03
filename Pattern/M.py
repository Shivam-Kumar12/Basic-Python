for row in range(6):
    for col in range(8):
        if (col==0 or col==7) or ((col==2 or  col==5)and(row==1)) or((col==3 or  col==4)and(row==2))or  col==3 and row==3 :
            print("*",end="")
        else:
            print(end=" ")
    print()