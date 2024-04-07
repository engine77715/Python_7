class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.last_name} {self.first_name}, {self.age} years old, {self.gender}'


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'Student: {super().__str__()}, record book: {self.record_book}'


class GroupOverflowError(Exception):
    def __init__(self, message="Максимальна кількість студентів у групі вже досягнута"):
        self.message = message
        super().__init__(self.message)


class Group:
    MAX_STUDENTS = 10

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= self.MAX_STUDENTS:
            raise GroupOverflowError()
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Number:{self.number}\n{all_students}'


# Тестування
st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 28, 'Bill', 'Gates', 'AN146')
gr = Group('PD1')

try:
    for _ in range(15):
        gr.add_student(Student('Male', 20, 'John', 'Doe', 'AN100'))
except GroupOverflowError as e:
    print(e)  # Максимальна кількість студентів у групі вже досягнута

gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)

print(gr)

gr.delete_student('Jobs')
print(gr)