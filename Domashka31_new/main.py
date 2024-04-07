from student import Student
from group import Group

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')

try:
    for _ in range(15):
        gr.add_student(Student('Male', 20, 'John', 'Doe', 'AN100'))
except GroupOverflowError as e:
    print(e)  # Максимальна кількість студентів у групі вже досягнута

gr.add_student(st1)
gr.add_student(st2)

print(gr)

print(gr.find_student('Jobs') == st1)  # 'Steve Jobs'
print(gr.find_student('Jobs2') is None)

gr.delete_student('Taylor')
print(gr)  # Only one student