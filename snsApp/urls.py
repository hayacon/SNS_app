from django.urls import include, path
from . import views
from . import api

urlpatterns = [
    path('signup/', views.register, name='signup' ),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
