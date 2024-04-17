from django.urls import path,include
from rest_framework.routers import DefaultRouter
from lms.dasboard.views import CountBook_View,Count_IssuedBook_View,Count_ToadyIssuedBook_View,CountStudent_View,CountStaff_View,Count_ToadyReturnBook_View,List_IssuedBook_View,List_ReturnBook_View



router = DefaultRouter()



urlpatterns = [
    path('', include(router.urls)),
    path('count_book/',CountBook_View.as_view()),
    path('count_student/',CountStudent_View.as_view()),
    path('count_staff/',CountStaff_View.as_view()),
    path('issued_book_count/',Count_IssuedBook_View.as_view()),
    path('todayissued_book_count/',Count_ToadyIssuedBook_View.as_view()),
    path('todayreturn_book_count/',Count_ToadyReturnBook_View.as_view()),
    path('list_issuedbook/',List_IssuedBook_View.as_view()),
    path('list_returnbook/',List_ReturnBook_View.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
