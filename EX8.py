class Student:
    count = 0
    def __init__(self, name):
        self.name, self.marks = name, [int(input(f"Enter marks for {name} in subject {i+1}: ")) for i in range(3)]
        Student.count += 1

    def display(self):
        print(f"{self.name} got {self.marks}")


s1 = Student(input("Enter the name of Student: "))
s2 = Student(input("Enter the name of Student: "))
print(f"\nNumber of students in class: {Student.count}")
s1.display()
s2.display()
