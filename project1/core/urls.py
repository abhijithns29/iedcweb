from django.urls import path,include
from django.contrib.auth import views as auth_views

from .import views
from .form import loginForm
app_name ='core'

urlpatterns =[
    path('',views.index,name='index'),
    path('contact/',views.contact,name="contact"),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.log_out,name='logout'),
    path('login/',auth_views.LoginView.as_view(template_name='core/login.html',authentication_form=loginForm),name="login"),
]