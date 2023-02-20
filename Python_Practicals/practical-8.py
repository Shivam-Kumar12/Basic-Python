n=int(input("Enter the Number:"))
temp=n
a=0
while temp>0:
    b=temp%10
    a=a*10+b
    temp=temp//10
print("the Reverse number is ",a)