class programmer():
    company="microsoft"

    def __init__(self,name,product):
        self.name=name
        self.product=product

    def programmerlist(self):
        print(f"the name of the programmer {self.name}")
        print(f" he programmer is engaged with the product is{self.product}")


harry=programmer("harry", "youtube")
shivam=programmer("shivam", "google")

harry.programmerlist()
shivam.programmerlist()