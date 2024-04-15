from django.urls import path
from lms.report.views import LocationReport_View,IssuedBookReport_View,ReturnBookReport_View,DueBookReport_View,DueAllBookReport_View

urlpatterns = [
    path('location_report/',LocationReport_View.as_view()),
    path('issue_report/',IssuedBookReport_View.as_view()),
    path('return_report/',ReturnBookReport_View.as_view()),
    path('due_bookreport/',DueBookReport_View.as_view()),
    path('due_allbook/',DueAllBookReport_View.as_view()),
]