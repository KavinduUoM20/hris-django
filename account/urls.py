from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('my-profile/',views.view_account, name="view_account"),
    path('add-profile/',views.add_profile, name="add_profile"),
    path('edit-profile/',views.edit_profile, name="edit_profile"),
]