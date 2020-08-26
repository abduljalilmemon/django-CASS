from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator, MinValueValidator 
from datetime import date
from django.utils import timezone  

# Create your models here.
sex_choice = (('Male', 'Male'),('Female', 'Female'))
class_choice =(('11','11'),('12','12'))
section_choice=(('A','A'),('B','B'),('C','C'))
DAY_OF_THE_WEEK = {
    ('Monday','Monday'),
    ('Tuesday','Tuesday'),
    ('Wednesday','Wednesday'),
    ('Thursday','Thursday'),
    ('Friday','Friday'),
    ('Saturday','Saturday')}
subject_choice=(
    ('Mathematics','Mathematics'),
    ('Botany','Botany'),
    ('Zoology','Zoology'),
    ('English','English'),
    ('Urdu','Urdu'),
    ('Physics','Physics'),
    ('Pakistan-Studies','Pakistan-Studies'),
    ('Computer-Science','Computer-Science'))
month_c=(
    ('January','January'),
    ('February','February'),
    ('March','March'),
    ('April','April'),
    ('May','May'),
    ('June','June'),
    ('July','July'),
    ('August','August'),
    ('September','Sepember'),
    ('October','October'),
    ('November','November'),
    ('December','December'))
att_choice=(
    ('Present','Present'),
    ('Absent','Absent'),
    ('Leave','Leave'))
dpt_choice=(
    ('Pre-Medical','Pre-Medical'),
    ('Pre-Engineering','Pre-Engineering'),
    ('Pre-Computer Science','Pre-Computer Science'))
class User(AbstractUser):
    @property
    def is_student(self):
        if hasattr(self, 'student'):return False
        return False
    @property
    def is_teacher(self):
        if hasattr(self, 'teacher'):return False
        return False
class Dept(models.Model):
    id = models.CharField(primary_key='True', max_length=100)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
class Course(models.Model):
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=20)
    def __str__(self):
        return (self.name+"-"+self.code)
class Class(models.Model):
    # courses = models.ManyToManyField(Course, default=1)
    class_no = models.CharField(choices=class_choice, default=9,max_length=2)
    dept = models.CharField(choices=dpt_choice,max_length=100,default='Bio')
    section = models.CharField(choices=section_choice,max_length=2,default='A')
    def __str__(self):
        return (self.class_no+"-"+self.dept+"-"+self.section)
class Student(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    classno = models.ForeignKey(Class, on_delete=models.CASCADE, default='9')
    name = models.CharField(max_length=200)
    fname = models.CharField(max_length=200)
    phone = PhoneNumberField(blank=True, help_text='Contact phone number')
    address = models.CharField(max_length=200,default='F-11, Markaz')
    sex = models.CharField(max_length=50, choices=sex_choice, default='Male')
    fee = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100000)])
    DOB = models.DateField(default='2005-01-01')
    def __str__(self):
        return self.name
class Teacher(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    phone = PhoneNumberField(blank=True, help_text='Contact phone number')
    address = models.CharField(max_length=200)
    sex = models.CharField(max_length=50, choices=sex_choice, default='Male')
    subject = models.CharField(max_length=50, choices=subject_choice, default='Math')
    salary = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100000)])
    DOB = models.DateField(default='1990-01-01')
    about =models.CharField(max_length=1000, default="Hello")
    def __str__(self):
        return self.name
class SubjectTeacher(models.Model):
    subject = models.ForeignKey(Course, on_delete=models.CASCADE)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.pk)
class Fee(models.Model):
    Student = models.ForeignKey(User, on_delete=models.CASCADE)
    status =  models.BooleanField(default=False)
    fee = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100000)])
    month = models.CharField(max_length=10,choices=month_c, default='March')
    d_date = models.DateField(default=date.today())
    pay_date = models.DateField(default=date.today())
class Mark(models.Model):
    name = models.CharField(max_length=20,default='Monthly Test')
    total_marks = models.IntegerField(default=0,validators=[MinValueValidator(1.0), MaxValueValidator(500.0)])
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=date.today())
    obtained = models.FloatField(default=0,validators=[MinValueValidator(0.0), MaxValueValidator(500.0)])
    classi = models.ForeignKey(SubjectTeacher, on_delete=models.CASCADE, default=1)
class Attendance(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    attendanceclass = models.ForeignKey(SubjectTeacher, on_delete=models.CASCADE, default=1)
    date = models.DateField(default=date.today())
    status = models.CharField(max_length=20,choices=att_choice,default='Absent')
class Announcement(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50,default="None")
    date_posted = models.DateTimeField(default=timezone.now)
    content = models.TextField()
class Time(models.Model):
    s_time = models.TimeField()
    e_time = models.TimeField()
    classname = models.ForeignKey(Class, on_delete=models.CASCADE, default='9')
    day = models.CharField(max_length=20,choices=DAY_OF_THE_WEEK,default='Monday')
    def __str__(self):
        return "("+str(self.classname)+") "+str(self.s_time)+" to "+str(self.e_time)+" "+self.day
class Timetable(models.Model):
    classtime =  models.OneToOneField(Time,primary_key=True, on_delete=models.CASCADE)
    subject = models.ForeignKey(Course, on_delete=models.CASCADE, default=1)
