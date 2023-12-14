from django.urls import path
from . import views


app_name = "teacher_438"
urlpatterns = [
    path('', views.index, name="index"),
    path('profile', views.profile, name='profile'),
    path('accounts/logout/', views.logout_view, name='logout'),

]