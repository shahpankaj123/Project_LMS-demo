from django.urls import path
from lms.Config.views import BarcodeImageView,CreateAuthor_View,CreatePublisher_View,CreateSupplier_View,CreateSubject_View,CreateLanguage_View,CreateEditor_View,CreateBook_Type_View,CreateRemark_View,CreateLocation_View



urlpatterns = [
    path('barcode_image/<int:pk>/', BarcodeImageView.as_view()),
    path('create-author/',CreateAuthor_View.as_view()),
    path('create-publisher/',CreatePublisher_View.as_view()),
    path('create-supplier/',CreateSupplier_View.as_view()),
    path('create-subject/',CreateSubject_View.as_view()),
    path('create-language/',CreateLanguage_View.as_view()),
    path('create-editor/',CreateEditor_View.as_view()),
    path('create-book_type/',CreateBook_Type_View.as_view()),
    path('create-remarks/',CreateRemark_View.as_view()),
    path('create-location/',CreateLocation_View.as_view()),
]

