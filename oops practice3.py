class train():
    def __init__(self, name,fare,seats):
        self.name=name
        self.seats=seats
        self.fare=fare
    def booktickets(self):
        if(self.seats>0):
            print(f"you can book the tickets {self.seats}")
            self.seats=self.seats-1
        else:
            print("the seats are reserved")
    def gtstatus(self):
        print(f"the name of the train is {self.name} ")
        print(f"The seats are available in the train is {self.seats}")
        
    def getfare(self):
      print(f"the fare for this train is {self.fare}")


Rajdhani=train("Rajdhani Express", 1234,12)
Rajdhani.gtstatus()
Rajdhani.getfare()
Rajdhani.booktickets()
Rajdhani.gtstatus()