n=int(input("enter total no:"))
x=1
for i in range(0,n):
    a=int(input("Enter a num:"))
    x=(1+a)*x
# for i in range(0,n):
# print("ans=",x)
ans=x**(1/n)-1
print("mean",ans)