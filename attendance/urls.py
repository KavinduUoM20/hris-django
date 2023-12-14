from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='attendance'),
    path('add-attendance/', views.add_attendance, name='add_attendance'),
    path('view-attendance/', views.view_attendance, name='view_attendance'),
    path('my-attendance/', views.my_attendance, name='my_attendance'),
    path('update-attendance/', views.update_attendance, name='update_attendance'),
]
