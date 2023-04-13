class Magari:
    def __init__(self,make,model,year):
        self.mymake=make
        self.mymodel=model
        self.myyear=year
    def kuanzisha(self):
        print(f"{self.mymake} {self.mymodel} {self.myyear} started")
class Toyota(Magari):
    def __init__(self,make,model,year,num_doors):
        super().__init__(make,model,year)
        self.mynum_door=num_doors
    def kuanzisha(self):
        print(f"{self.mymake} {self.mymodel} {self.myyear} car with {self.mynum_door} doors started")
gari=Toyota("Premio","saloon",2023,5)
gari.kuanzisha()

