n = input("Enter Number to calculate sum & average:")
n = int (n)
sum = 0
for i in range(1,n+1,1):
    sum = sum+i
    # num=num+1
average = sum / n

print("SUM of", n, "numbers is: ", sum )
print("Average of", n, "natural number is: ", average)



#                OR

def Averagelist(list):
    return sum(list)/len(list)

list=[1,2,3,4,5,6,7,8,9,10]
average=Averagelist(list)
print("the average of the list is:",+average)