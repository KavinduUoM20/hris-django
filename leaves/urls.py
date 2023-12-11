from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="leaves"),
    path('add-leaves', views.add_leaves, name="add_leaves"),
    path('view-leaves', views.view_leaves, name="view_leaves"),
    path('my-leaves/', views.my_leaves, name='my_leaves'),
    path('update-leave/<int:leave_id>/', views.update_leave, name='update_leave'),
]
