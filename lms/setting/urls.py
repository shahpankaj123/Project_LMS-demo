from django.urls import path
from lms.setting.views import FineSetting_View,BookType_View,DeleteFineSetting_View
urlpatterns = [
    path('',FineSetting_View.as_view()),
    path('<int:id>/',DeleteFineSetting_View.as_view()),
    path('get_booktype/',BookType_View.as_view())
]