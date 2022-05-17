from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages 
from .models import Announcement, Teacher, SubjectTeacher, Student, Attendance, User,Mark,Fee, Timetable, Time
from django.http import HttpResponseRedirect
from django.utils import timezone  
import datetime

# Create your views here.
def login(request):
    _message = 'Please sign in'
    a='info/s_login.html'
    if request.method == 'POST':
        _username = request.POST.get('username')
        _password = request.POST.get('password')
        user = authenticate(username=_username, password=_password)
        print(user)
        if user is not None and hasattr(user, 'student'):
            if user.is_active:
                auth_login(request, user)
                ancmnt= Announcement.objects.all()
                return render(request,'info/s_homepage.html',{'ancmnt': ancmnt})
            else:
                _message = 'Your account is not activated'
        else:
            _message = 'Invalid username or password, please try again.'
        
    context = {'message': _message}
    return render(request,a,context)
def t_login(request):
    _message = 'Please sign in'
    if request.method == 'POST':
        _username = request.POST.get('username')
        _password = request.POST.get('password')
        user = authenticate(username=_username, password=_password)
        if user is not None and hasattr(user, 'teacher'):
            if user.is_active:
                auth_login(request, user)
                ancmnt= Announcement.objects.all()
                return render(request,'info/t_homepage.html',{'ancmnt': ancmnt})
            else:
                _message = 'Your account is not activated'
        else:
            _message = 'Invalid username or password, please try again.'
    context = {'message': _message}
    return render(request, 'info/t_login.html',context)
@login_required
def t_profile(request):
    return render(request ,'info/t_profile.html')
@login_required
def s_profile(request):
    return render(request ,'info/s_profile.html')
@login_required
def index(request):
    if request.user.is_teacher:
        return render(request, 'info/t_homepage.html')
    if request.user.is_student:
        return render(request, 'info/t_homepage.html')
    return render(request, 'info/logout.html')
def capitalizing(text):
    new = text.split()
    arr = []
    for i in new:
        i = i[0].upper() + i[1:]
        arr.append(i)
    str = " ".join(arr)
    return str
@login_required
def t_update(request):
    _message = ''
    if request.method == 'POST':
        name = request.POST.get('fname')
        address = request.POST.get('address')
        print(address)
        mobile = request.POST.get('mobile')
        aboutl = request.POST.get('about')
        name = capitalizing(name)
        address = capitalizing(address)
        print(address)
        if name != "":request.user.teacher.name=name
        if address != "":request.user.teacher.address=address
        if mobile != "":request.user.teacher.phone=mobile
        if aboutl != "":
            if aboutl[0].islower():aboutl = aboutl[0].upper() + aboutl[1:]
            request.user.teacher.about=aboutl
        print(request.user.teacher.name,address)
        request.user.teacher.save()
        _message='Your profile is updated succesfully'
    context = {'message': _message}
    return render(request,'info/t_profile.html',context)
@login_required
def t_password(request):
    _message = 'Note: please match your old and new password'
    if request.method == 'POST':
        _password = request.POST.get('old_pass')
        new = request.POST.get('new_pass')
        con = request.POST.get('conf_pass')
        print(new,_password)
        user = authenticate(username=request.user.username, password=_password)
        if user is not None:
            _message='Your Password does not match.'
            if new==con:
                _message="Successfully your password is changed"
                request.user.set_password(new)
                request.user.save()
    context = {'message': _message}
    return render(request,'info/t_pass.html',context)
@login_required
def s_password(request):
    _message = 'Note: please match your old and new password'
    if request.method == 'POST':
        _password = request.POST.get('old_pass')
        new = request.POST.get('new_pass')
        con = request.POST.get('conf_pass')
        print(new,_password)
        user = authenticate(username=request.user.username, password=_password)
        if user is not None:
            _message='Your Password does not match.'
            if new==con:
                _message="Successfully your password is changed"
                request.user.set_password(new)
                request.user.save()
            
    context = {'message': _message}
    return render(request,'info/s_pass.html',context)
@login_required
def s_marks(request):
    class_n=request.user.student.classno
    a=SubjectTeacher.objects.filter(class_name=class_n)
    arr=[]
    for i in a:
        att=Mark.objects.filter(student=request.user,classi=i)
        for j in att:
            print(j.total_marks,i.subject,j.name)
        arr.append(att)
    return render(request,'info/s_marks.html',{'subj':a,'att':arr})
@login_required
def s_attendance(request):
    class_n=request.user.student.classno
    a=SubjectTeacher.objects.filter(class_name=class_n)
    arr=[]
    for i in a:
        att=Attendance.objects.filter(student=request.user,attendanceclass=i)
        for j in att:
            print(j.status,i.subject,j.date)
        arr.append(att)
    print(arr)
    return render(request,'info/s_attendance.html',{'subj':a,'att':arr})
@login_required
def t_timetable(request): 
    a=SubjectTeacher.objects.filter(teacher=request.user)
    arr=[]
    for i in a:
        time=Time.objects.filter(classname=i.class_name)
        print(i.class_name,i.subject)
        subj=i.subject
        for j in time:
            timetable=Timetable.objects.filter(classtime=j,subject=subj)
            for k in timetable:
                print(k.classtime)
                arr.append(k)
    return render(request,'info/t_timetable.html',{'time':arr,'s_t':datetime.time(8, 30),
                                                                's_t1':datetime.time(9, 30),
                                                                's_t2':datetime.time(11, 00),
                                                                's_t3':datetime.time(12, 00),
                                                                's_t4':datetime.time(13, 00)})
@login_required
def t_student(request):
    a=SubjectTeacher.objects.filter(teacher=request.user)
    arr=[]
    arr1=[]
    for i in a:
        c=i.class_name
        arr1.append(c)
        b=Student.objects.filter(classno=c)
        arr.append(b)
    return render(request,'info/t_student.html',{'stu': arr,'class':arr1})
@login_required
def t_homepage(request):
    ancmnt= Announcement.objects.all()
    return render(request,'info/t_homepage.html',{'ancmnt': ancmnt})
@login_required
def s_homepage(request):
    ancmnt= Announcement.objects.all()
    return render(request,'info/s_homepage.html',{'ancmnt': ancmnt})
@login_required
def s_fee(request):
    fe=Fee.objects.filter(Student=request.user)
    return render(request ,'info/s_fee.html',{'fee': fe})
@login_required
def s_report(request):
    marks=Mark.objects.filter(student=request.user)
    subj=SubjectTeacher.objects.filter(class_name=request.user.student.classno)
    at=[]
    mk=[]
    att=Attendance.objects.filter(student=request.user)
    date_month=timezone.datetime.today().month
    if  request.method == 'POST':
        option=request.POST.get('option')
        print(option)
        date_month=option
    arr1=[]
    for j in subj:
        ttl=0
        prs=0
        for k in att:
            if int(k.date.month)==int(date_month) and j.subject==k.attendanceclass.subject :
                ttl+=1
                if k.status=='Present':
                    prs+=1
        if ttl==0:
            ttl=1
            prs=0
        at.append((prs/ttl)*100) 
    for i in marks:
        if not i.date.month in arr1:
            arr1.append(i.date.month)
        if int(i.date.month)==int(date_month):
            mk.append(i)
    arr1.sort()
    print(mk)
    return render(request ,'info/s_report.html',{'ad':mk,'sub':subj,'at':at,'arr':arr1})
@login_required
def t_marks(request):
    _message='Note: Enter correct marks.'
    aa=SubjectTeacher.objects.filter(teacher=request.user)
    arr=[]
    arr1=[]
    for i in aa:
        c=i.class_name
        arr1.append(c)
        b=Student.objects.filter(classno=c)
        arr.append(b)
        a=i
    if request.method == 'POST':
        stat=request.POST.get('topic')
        tot=int(request.POST.get('Obtained'))
        dat=request.POST.get('day')
        for i in arr:
            for sre in i:
                wq=str(sre.username)
                if request.POST.get(wq):
                    mark=int(request.POST.get(wq))
                    print(wq)
                    if mark>tot:
                        _message = 'Error!! Enter correct marks'
                        return render(request,'info/t_marks.html',{'st': arr,'class':arr1,'message': _message})  
        for i in arr:
            for stu in i:
                wq=str(stu.username)
                mark=request.POST.get(wq)
                if request.POST.get(wq):
                    print(tot,stu.username,mark)
                    a=SubjectTeacher.objects.get(teacher=request.user,class_name=stu.classno)
                    stat = stat.capitalize()
                    ms=Mark(name=stat,total_marks=tot,date=dat,student=stu.username,obtained=mark,classi=a)
                    ms.save()
                    _message = 'Marks updated successfully!'
    return render(request,'info/t_marks.html',{'st': arr,'class':arr1,'message': _message})
@login_required
def t_reports(request):
    name = request.POST.get('name')
    b=User.objects.get(username=name)
    c=Student.objects.get(username=b)
    a=SubjectTeacher.objects.get(teacher=request.user,class_name=c.classno)
    er=Mark.objects.filter(student=b,classi=a)
    wef=Attendance.objects.filter(student=b,attendanceclass=a)
    count1=0
    prs=0
    print(b,a)
    for i in wef:
        count1+=1
        if i.status=='Present':
            prs+=1
    wr=rw=0
    count = 0
    for i in er:
        print(i.name,i.student,i.total_marks)
        count+=1
        wr=wr+i.obtained
        rw=rw+i.total_marks
    return render(request ,'info/t_reports.html',{'stu': c,'subj':a,'ad':er,'avg':wr,'t_att':count1,'t_prs':prs,'t_rw':prs+rw,'t_to':wr+prs})
@login_required
def t_attendance(request):
    _message = ''
    a=SubjectTeacher.objects.filter(teacher=request.user)
    arr=[]
    arr1=[]
    for i in a:
        c=i.class_name
        arr1.append(c)
        b=Student.objects.filter(classno=c)
        arr.append(b)
    if request.method == 'POST':
        dat=request.POST.get('day')
        for i in arr:
            for stu in i:
                wq=str(stu.username)
                status1=request.POST.get(wq) 
                if status1 :
                    acc=SubjectTeacher.objects.get(teacher=request.user,class_name=stu.classno)
                    a = Attendance(attendanceclass=acc,date=dat, student=stu.username, status=status1)
                    a.save()
                    _message = 'Attendance updated successfully!'
                    print(a.student,a.status,a.date)
    return render(request,'info/t_attendance.html',{'st': arr,'class':arr1,'message': _message})
@login_required
def t_ancmnt(request):
    if request.method == 'POST':
        idw = request.POST.get('ide')
        if idw != None:
            print(idw)
            ab=Announcement.objects.get(id=idw)
            ab.delete()
            ancmnt= Announcement.objects.all()
            return render(request,'info/t_homepage.html',{'ancmnt': ancmnt})
        titls = request.POST.get('titl')
        contnts = request.POST.get('contnt')
        titls = capitalizing(titls)
        now = timezone.now()
        if contnts[0].islower():
            contnts = contnts[0].upper() + contnts[1:]
        ann = Announcement(username=request.user,title=titls,date_posted=now, content=contnts)
        ann.save()
        print(titls,contnts,now)
    return render(request,'info/t_ancmnt.html')
@login_required
def s_timetable(request):
    class_n = request.user.student.classno
    time=Time.objects.filter(classname=class_n)
    arr=[]
    for i in time:
        timetable=Timetable.objects.get(classtime=i)
        print(timetable.subject,i.s_time,i.e_time,timetable.classtime.classname)
        arr.append(timetable)
    return render(request ,'info/s_timetable.html',{'time':arr,'s_t':datetime.time(8, 30),
                                                                's_t1':datetime.time(9, 30),
                                                                's_t2':datetime.time(11, 00),
                                                                's_t3':datetime.time(12, 00),
                                                                's_t4':datetime.time(13, 00)}
    )

