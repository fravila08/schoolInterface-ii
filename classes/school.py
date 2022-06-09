from classes.staff import Staff
from classes.student import Student

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.objects()
        self.students = Student.objects()

    def list_students(self):
        print('\n')
        for i, student in enumerate(self.students):
            print(f'{i + 1}. {student.name} {student.school_id}')

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.school_id == student_id:
                return student
            
    def add_student(self, student):
        self.students.append(Student(**student))

    def delete_student(self,student):
        validation=input('Plese enter the student Password')
        if validation == student.password:
            self.students.remove(student)
        else:
            raise(f'This is an incorrect password')