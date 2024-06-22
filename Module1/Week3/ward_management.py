class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name)
        self.yob = yob
        self.grade = grade

    def describe(self):
        print(f">>> {self.__class__.__name__}")
        print(f"Name: {self.name} - YoB: {self.yob} - Grade: {self.grade}")

class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name)
        self.yob = yob
        self.subject = subject

    def describe(self):
        print(f">>> {self.__class__.__name__}")
        print(f"Name: {self.name} - YoB: {self.yob} - Subject: {self.subject}")


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name)
        self.yob = yob
        self.specialist = specialist

    def describe(self):
        print(f">>> {self.__class__.__name__}")
        print(f"Name: {self.name} - YoB: {self.yob} - Specialist: {self.specialist}")

class Ward:
    def __init__(self, name):
        self.name = name
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def describe(self):
        print(f">>> Ward")
        print(f"Name: {self.name}")
        for person in self.people:
            person.describe()

    def count_doctor(self):
        count = 0
        for person in self.people:
            if isinstance(person, Doctor):
                count += 1
        return count

    def sort_age(self):
        self.people.sort(key=lambda person: person.yob)

    def compute_average_yob_teacher(self):
        yobs = []
        for person in self.people:
            if isinstance(person, Teacher):
                yobs.append(person.yob)
        if not yobs:
            return None
        return sum(yobs) / len(yobs)

student1 = Student("studentA", 2010, "7")
student1.describe()

teacher1 = Teacher("teacherA", 1969, "Math")
teacher1.describe()

doctor1 = Doctor("doctorA", 1945, "Endocrinologists")
doctor1.describe()


ward1 = Ward("Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(Doctor("doctorB", 1975, "Cardiologists"))
ward1.add_person(Teacher("teacherB", 1995, "History"))

ward1.describe()

print(f"Number of docters: {ward1.count_doctor()}")

ward1.sort_age()
ward1.describe()

average_yob_teacher = ward1.compute_average_yob_teacher()
if average_yob_teacher is not None:
    print(f"Average year of birth (teachers): {average_yob_teacher}")
else:
    print("There is none teacher in ward")
