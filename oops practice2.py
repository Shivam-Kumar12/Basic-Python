class calculator():
    def __init__(self,num):
        self.num=num

    def square(self):
        print(f"the square of the number {self.num} is {self.num **2}")
    
    def squareroot(self):
        print(f"the squareroot of the number {self.num} is {self.num **0.5}")
        pass
    def cube(self):
        print(f"the cube of the number {self.num} is {self.num **3}")
    
    @staticmethod
    def greet():
        print("hello users")
    
a=calculator(9)
a.greet()
a.square()
a.cube()
a.squareroot()
