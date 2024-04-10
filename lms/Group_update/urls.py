from django.urls import path,include
from lms.Group_update.views import UpdateSubjectView,UpdateLocationView,UpdateRemarksView,UpdateSupplierView,UpdatePublisherView,UpdateBookTypeView



urlpatterns = [
    path('update-subject/', UpdateSubjectView.as_view()),
    path('update-location/', UpdateLocationView.as_view()),
    path('update-remarks/',UpdateRemarksView.as_view()),
    path('update-supplier/',UpdateSupplierView.as_view()),
    path('update-publisher/',UpdatePublisherView.as_view()),
    path('update-booktype/',UpdateBookTypeView.as_view()),
]    