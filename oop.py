class Fruits:
    def __init__(self, type, color, price):
        self.mytype = type
        self.mycolor = color
        self.myprice = price

    def onyesha(self):
        print(self.mytype, self.mycolor, self.myprice)

    def maji(self):
        print(self.mytype, self.mycolor, self.myprice)

    def hello(self):
        print(self.mytype, self.mycolor, self.myprice)

    def sasa(self):
        print(self.mytype, self.mycolor, self.myprice)


# create an object
myobj = Fruits("Banana ", "Yellow ", 20)
myobject=Fruits("Mangoes ","Red yellow ",30)
myother=Fruits("Orange ","Orange ",15)
mylast=Fruits("Apple ","Green ",30)
myobj.onyesha()
myobject.maji()
myother.hello()
mylast.sasa()

class Employees:
    def __init__(self, Name, Salary):
        self.thename=Name
        self.thesalary=Salary
    def first(self):
        print(self.thename,self.thesalary)

    def second(self):
        print(self.thename, self.thesalary)
theobject=Employees("Erick Were ", 120000)
theobject.first()
another=Employees("George Bush ",100000)
another.second()
