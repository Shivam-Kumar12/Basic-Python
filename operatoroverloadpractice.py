class complex:
    def __init__(self,r,i):
        self.real=r
        self.imaginary=i
    def __add__(self,c):
        return complex(self.real+ c.real, self.imaginary + c.imaginary)
    
    def __mul__(self,c):
        mulreal=self.real+ c.real-self.imaginary + c.imaginary
        mulimaginary=self.real+ c.imaginary - self.imaginary + c.real
        return complex(mulreal,mulimaginary)

    def __str__(self):
        return f"{self.real}+{self.imaginary}i"

c1=complex(1, 2)
c2=complex(6, 4)
print(c1+c2)
print(c1*c2)