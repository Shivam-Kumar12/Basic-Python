n = input("Enter Number to calculate sum & average:")
num=0
n = int (n)

sum = 0

while num<=n:
    sum = sum+num
    num=num+1
average = sum / n

print("SUM of", n, "numbers is: ", sum )
print("Average of", n, "natural number is: ", average)