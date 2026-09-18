class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll:", self.roll)
        print("Marks:", self.marks)

name = input("Enter student name: ")
roll = int(input("Enter roll number: "))
marks = float(input("Enter marks: "))

s = Student(name, roll, marks)
s.display()
