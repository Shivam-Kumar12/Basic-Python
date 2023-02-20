a=float(input("enter coefficient of x^2="))
b=float(input("enter coefficient of x="))
c=float(input("enter constant="))
print("the quadratic equation is ",a,"x^2+",b,"x+",c)
D=b**2-4*a*c

r1=(-b+(D)**(0.5))/2*a
r2=(-b-(D)**(0.5))/2*a

print("root1=",r1)
print("root2=",r2)