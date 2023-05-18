from django.urls import path
from django.contrib.auth import views as auth_views 
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('home/', views.home, name='home'),
    path('chat/<int:user_id>/', views.chat, name='chat'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
]
