from django.contrib import admin
from .models import Student,Teacher,User,Class,Course,Announcement,SubjectTeacher,Attendance,Mark,Fee,Time,Timetable
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','fname','phone','address','DOB','fee')
    search_fields = ('id', 'name')
    ordering = ['id', 'classno']
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','subject','phone','address','DOB','salary')
    search_fields = ('name', 'id','subject')
    ordering = ['id', 'name']
class ClassAdmin(admin.ModelAdmin):
    list_display=('id','class_no','dept','section')
    search_fields = ('class_no', 'id')
    ordering = ['id','class_no', 'section']
class CourseAdmin(admin.ModelAdmin):
    list_display=('id','code','name')
    search_fields = ('id', 'code')
    ordering = ['id','name']
class AnnouncementAdmin(admin.ModelAdmin):
    list_display=('id','username','title','date_posted')
    search_fields = ('id', 'username')
    ordering = ['date_posted']
class SubjectTeacherAdmin(admin.ModelAdmin):
    list_display=('id','subject','teacher','class_name')
    search_fields = ('class_name', 'teacher')
    ordering = ['class_name']
class AttendanceAdmin(admin.ModelAdmin):
    list_display=('student','date')
    search_fields = ('student','status')
    ordering = ['student']
class MarkAdmin(admin.ModelAdmin):
    list_display=('student','obtained','total_marks')
    search_fields = ('student','obtained')
    ordering = ['student']
class FeeAdmin(admin.ModelAdmin):
    list_display=('Student','fee','status','month')
    search_fields = ('Student','status')
    ordering = ['Student']
class TimeAdmin(admin.ModelAdmin):
    list_display=('s_time','e_time','classname')
    search_fields = ('s_time','e_time','classname')
    ordering = ['classname']
class TimetableAdmin(admin.ModelAdmin):
    list_display=('classtime','subject')
    search_fields = ('classtime','subject')
    ordering = ['subject']
admin.site.register(Time,TimeAdmin)   
admin.site.register(Timetable,TimetableAdmin)  
admin.site.register(Fee,FeeAdmin)   
admin.site.register(Mark,MarkAdmin)     
admin.site.register(Attendance,AttendanceAdmin)    
admin.site.register(SubjectTeacher,SubjectTeacherAdmin)
admin.site.register(Announcement,AnnouncementAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)