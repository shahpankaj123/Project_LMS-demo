from django.urls import path
from lms.manage_member.views import StudentList_View,SingleStudent_View,ActiveStudent_View,UpdateStatusStudent_View,CreateListStaff_View,UpdateStaff_View,CreateListVisitor_View,UpdateVisitor_View,List_InActiveVisitor_View,List_GuestVisitor_View

urlpatterns = [
    #student
    path('student_list/', StudentList_View.as_view()),
    path('singlestudent_list/<int:pk>/', SingleStudent_View.as_view()),
    path('activestudent/',ActiveStudent_View.as_view()),
    path('update-status/<int:pk>/',UpdateStatusStudent_View.as_view()),
    #staff

    path('listcreate_staff/',CreateListStaff_View.as_view()),
    path('update_staff/<int:pk>/',UpdateStaff_View.as_view()),

    #visitor
    path('listcreate_visitor/',CreateListVisitor_View.as_view()),
    path('update_visitor/<int:pk>/',UpdateVisitor_View.as_view()),
    path('listinactive_visitor/',List_InActiveVisitor_View.as_view()),
    path('listGuest_visitor/',List_GuestVisitor_View.as_view()),

]
