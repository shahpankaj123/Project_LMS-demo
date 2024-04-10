from django.urls import path,include
from lms.Group_update.views import UpdateSubjectView,UpdateLocationView,UpdateRemarksView,UpdateSupplierView,UpdatePublisherView,UpdateBookTypeView,UpdateStatusView,UpdateBill_Info_View,Update_No_of_page_View,Update_BookPriceView,Update_BookPublishedYear_View



urlpatterns = [
    path('update-subject/', UpdateSubjectView.as_view()),
    path('update-location/', UpdateLocationView.as_view()),
    path('update-remarks/',UpdateRemarksView.as_view()),
    path('update-supplier/',UpdateSupplierView.as_view()),
    path('update-publisher/',UpdatePublisherView.as_view()),
    path('update-booktype/',UpdateBookTypeView.as_view()),
    path('update-bookstatus/',UpdateStatusView.as_view()),
    path('update-bill_info/',UpdateBill_Info_View.as_view()),
    path('update-page_no/',Update_No_of_page_View.as_view()),
    path('update-book_published_year/',Update_BookPublishedYear_View.as_view()),
    path('update-book_price/',Update_BookPriceView.as_view()),
]    