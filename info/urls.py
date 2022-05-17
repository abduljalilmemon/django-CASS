from django.urls import path
from . import views
urlpatterns = [
    path('', views.login, name='login'),
    path('t_update',views.t_update, name='t_update'),
    path('t_ancmnt',views.t_ancmnt, name='t_ancmnt'),
    path('t_marks', views.t_marks, name='t_marks'),
    path('s_marks', views.s_marks, name='s_marks'),
    path('t_login', views.t_login, name='t_login'),
    path('t_reports',views.t_reports, name='t_reports'),
    path('s_profile',views.s_profile, name='s_profile'),
    path('t_profile',views.t_profile, name='t_profile'),
    path('t_student',views.t_student, name='t_student'),
    path('s_fee',views.s_fee, name='s_fee'),
    path('s_report',views.s_report, name='s_report'),
    path('s_attendance',views.s_attendance, name='s_attendance'),
    path('t_attendance',views.t_attendance, name='t_attendance'),
    path('t_password',views.t_password, name='t_password'),
    path('s_password',views.s_password, name='s_password'),
    path('s_homepage',views.s_homepage, name='s_homepage'),
    path('t_homepage',views.t_homepage, name='t_homepage'),
    path('s_timetable',views.s_timetable, name='s_timetable'),
    path('t_timetable',views.t_timetable, name='t_timetable')
]