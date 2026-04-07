#Class and Object

class Student:

    class_year = 2024
    num_of_std = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.num_of_std += 1

    def std(self):
        print(f"Student name is : {self.name} and age is : {self.age}")

student1 = Student("Mahesh",22)
student2 = Student("Kalyan",22)
student3 = Student("Chethan",24)
student4 = Student("Jeethu",23)

print(student2.name)
student2.std()
print(f"Number of students : {Student.num_of_std}")
