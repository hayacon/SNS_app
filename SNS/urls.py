"""SNS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

urlpatterns = [
    #path for api swaggerdocs
    path('swaggerdocs/', TemplateView.as_view(
        template_name='snsApp/swagger-docs.html',
        extra_context={"schema_url":"openapi-schema"}
    ), name='swagger-docs'),
    #path for open api schema
    path('apischema/', get_schema_view(
        title='snsApp REST API',
        description='API for interact with user data and post',
        version='1.0'
    ), name='openapi-schema'),
    path('admin/', admin.site.urls),
    path('', include('snsApp.urls')),
]
