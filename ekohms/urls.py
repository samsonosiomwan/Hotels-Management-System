from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rooms/', views.rooms, name='rooms'),
    path('rooms/<uuid:room_id>/', views.rooms_detailed_view, name='rooms_detailed_view'),
    path('rooms/<uuid:room_id>/booking/', views.booking, name='booking'),
    path('rooms/<uuid:room_id>/booking/payment/', views.payment, name='payment'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),

]
