from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name='members'),
    path('members/', views.members, name='members'),
    path('alifMobi/', views.alifMobi, name='alifMobi'),
    path('visa/', views.visa, name='visa'),
    path('salom/', views.salom, name='salom'),
    path('CarFinancing/', views.CarFinancing, name='CarFinancing'),
    path('alifShop/', views.alifShop, name='alifShop'),
    path('transfers/', views.transfers, name='transfers'),
    path('deposits/', views.deposits, name='deposits'),
    path('alifOnline/', views.alifOnline, name='alifOnline'),
]