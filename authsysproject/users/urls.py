from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_view



urlpatterns = [
    path('', views.home, name='home'),
    path('homepage/', views.homepage, name='homepage'),
    path('about/', views.about, name='about'),
    path('antenatal/', views.antenatal, name='antenatal'),
    path('blog_single/', views.blog_single, name='blog_single'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('delivery/', views.delivery, name='delivery'),
    path('doctors/', views.doctors, name='doctors'),
    path('postnatal/', views.postnatal, name='postnatal'),
    path('services/', views.services, name='services'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('chat_view/', views.chat_view, name='chat_view'),
    path('form/', views.form, name='form'),
    path('admin/', admin.site.urls),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
]