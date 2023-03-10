from django.urls import path
from .views import ItemList, ItemDetail, LocationList, LocationDetail

#urlpatterns = [
    #path('/<int:pk>', DetailMYSITEBASE2.as_view()),
    #path('', ListMYSITEBASE2.as_view()),
    #path('create', CreateMYSITEBASE2.as_view()),
    #path('delete', DeleteMYSITEBASE2.as_view()),
#]

urlpatterns = [
    path('item/', ItemList.as_view()),
    path('item/<int:pk>/', ItemDetail.as_view()),
    path('location/', LocationList.as_view()),
    path('location/<int:pk>/', LocationDetail.as_view()),
]