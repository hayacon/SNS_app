from django.urls import include, path
from . import views
from . import api
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.sidebar, name='home'),
    path('signup/', views.register, name='signup' ),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.user_profile, name='user_profile'),
    path('user_home/', views.user_home, name='user_home'),
    path('search_user/', views.search_user, name='search-user'),
    path('api/user/<str:username>/', api.UserList.as_view(), name='user-list'),
    path('api/posts/<int:pk>/', api.PostsList.as_view(), name='post'),
    path('api/posts/<str:username>/', api.UserPostList.as_view(), name='user_post'),
    path('api/post/', api.NewPostList.as_view(), name='new_post')
]

urlpatterns += static(settings.STATIC_URL)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
