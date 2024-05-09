from django.urls import path
from .views import *

urlpatterns = [
    path('items/list/', ItemListAPIView.as_view(), name='item-list'),
    path('items/create/', ItemCreateAPIView.as_view(), name='item-create'),
    path('items/detail/<int:pk>/', ItemRetrieveAPIView.as_view(), name='item-detail'),
    path('items/update/<int:pk>/', ItemUpdateAPIView.as_view(), name='item-update'),
    path('items/delete/<int:pk>/', ItemDeleteAPIView.as_view(), name='item-delete'),
]
