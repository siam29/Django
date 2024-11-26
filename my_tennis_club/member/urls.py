from django.urls import path
from . import views

urlpatterns = [
    path('member/', views.members, name='member'),
    path('member/details/<int:id>', views.details, name='details'),
    path('university/', views.university, name='university1'),
]