from django.urls import path
from lms.transction.views import Transction_View

urlpatterns = [
    path('',Transction_View.as_view()),
]

