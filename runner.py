from ast import Delete
from classes.school import School 

school = School('Ridgemont High') 

while True:
    mode = input("\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student <student_id>\n3. Add a Student\n4. Remove a Student <student_id>\n5. Quit\n")

    if mode == '1':
        school.list_students()
    elif mode == '2':
        student_id = input('Enter student id:')
        student_string = str(school.find_student_by_id(student_id))
        print(student_string)
    elif mode =='3':
        stud_data={'role': 'student'}
        stud_data['name']=input('Whats the students First Name?')
        stud_data['age']=input('What is the students age?')
        stud_data['school_id']=input('What is the students ID?')
        stud_data['password']=input('What is your wanted Password?') 
        school.add_student(stud_data)       
    elif mode == '4':
        student_id = input('Enter student id:')
        student_obj= (school.find_student_by_id(student_id))
        school.delete_student(student_obj)
    elif mode == '5':
        break
