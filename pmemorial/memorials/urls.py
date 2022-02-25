from django.urls import path
from .views import MemorialCreate, MemorialDelete, MemorialUpdate, MemorialDetail, MemorialList

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('memorial/list', MemorialList.as_view(), name='memorial-list'),
    path('memorial/add', MemorialCreate.as_view(), name='memorial-add'),
    path('memorial/update/<int:pk>/', MemorialUpdate.as_view(), name='memorial-update'),
    path('memorial/delete/<int:pk>', MemorialDelete.as_view(), name='memorial-delete'),
    path('memorial/detail/<int:pk>/', MemorialDetail.as_view(), name='memorial-detail'),
    path('payment', views.payment, name='payment'),
    path('process_donation', views.process_donation, name='process-donation'),
    path('past-donations', views.past_donations, name='past-donations'),
]