from django.urls import path
from lms.manage_member.views import StudentList_View,SingleStudent_View,ActiveStudent_View,UpdateStatusStudent_View

urlpatterns = [
    path('student_list/', StudentList_View.as_view()),
    path('singlestudent_list/<int:pk>/', SingleStudent_View.as_view()),
    path('activestudent/',ActiveStudent_View.as_view()),
    path('update-status/<int:pk>/',UpdateStatusStudent_View.as_view())
]
