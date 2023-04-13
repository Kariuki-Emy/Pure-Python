class Person:
    def __init__(self, name, age, ):
        self.myname = name
        self.myage = age

    def habari(self):
        print("My name is " + self.myname)


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age, )
        self.mystudent = student_id
        self.myage = age

    def habari(self):
        super().habari()
        print("I am a student with ID " + str(self.mystudent) + " " + "whose age is " + str(self.myage))


myname = Student("Erick", 30, 12345)
myname.habari()
