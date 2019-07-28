from django.urls import path
from Autentificacion import views

urlpatterns = [
    path('login/', views.auth_login, name="loggin"),
    path('logout/', views.auth_logout, name="loggout"),
]
