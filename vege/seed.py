from faker import Faker
fake = Faker()
import random
from .models import *
from django.db.models import Sum

def create_subject_marks(n):
    try:
        students = Student.objects.all()
        subjects = Subject.objects.all()
        
        for student in students:
            for subject in subjects:
                if not SubjectMarks.objects.filter(student=student, subject=subject).exists():
                    SubjectMarks.objects.create(subject=subject, student=student, marks=random.randint(0, 100))
    
    except Exception as e:
        print("An error occurred:", e)
    
    print("Subject marks creation completed.")



def seed_db(n=10)->None:
    try:
        for i in range(n):
            department_objs = Department.objects.all()
            random_index= random.randint(0,len(department_objs)-1)

            department = department_objs[random_index]
            student_id = f'STU--{random.randint(100,999)}'

            student_name =fake.name()
            student_email = fake.email()
            student_age = random.randint(20,30)
            student_address = fake.address()

            student_id_obj = StudentID.objects.create(student_id= student_id)

            student_obj = Student.objects.create(
                department  = department,
                student_id = student_id_obj,
                student_name =  student_name,
                student_email = student_email,
                student_age = student_age,
                student_address = student_address
            )

    except Exception as e:
        print(e)


def generate_report_card():
    ranks = Student.objects.annotate(marks = Sum('studentmarks__marks')).order_by('-marks' ,'-student_age')
    i= 1
    for rank in ranks:
        ReportCard.objects.create(
            student = rank , 
            student_rank = i)
        i+=1