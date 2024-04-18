from django.urls import path
from lms.transction.views import Transction_View,AdvancedSearchBook_View,IssuedBook_View,ReturnBook_View

urlpatterns = [
    path('',Transction_View.as_view()),
    path('search_book/',AdvancedSearchBook_View.as_view()),
    path('issuedbook/<pk>/',IssuedBook_View.as_view()),
    path('returnbook/<pk>/',ReturnBook_View.as_view())
]

