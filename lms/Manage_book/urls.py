from django.urls import path
from lms.Manage_book.views import Create_SeriesBookView,Create_CustomBookView,BookSummary_UodateView,AdvancedSearchBook_View,BookImg_UodateView,UpdateBook_View

urlpatterns = [
    path('create_SeriesBook/',Create_SeriesBookView.as_view()),
    path('create_customBook/',Create_CustomBookView.as_view()),
    path('Update_book/<int:pk>/',UpdateBook_View.as_view()),
    path('Update_BookDesc/',BookSummary_UodateView.as_view()),
    path('advanced_Booksearch/',AdvancedSearchBook_View.as_view()),
    path('update_bookimg/',BookImg_UodateView.as_view()),

]