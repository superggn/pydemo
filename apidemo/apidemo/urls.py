"""
URL configuration for apidemo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from demo.views import EchoView, ExampleView, HelloWorldView

urlpatterns = [
    path('admin/', admin.site.urls),
    # 注意， 生产环境不能加这几个 url
    path('api/schema/', SpectacularAPIView.as_view(), name='schemahaha'),  # OpenAPI schema
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schemahaha'), name='swagger-ui'),  # Swagger UI
    path('api/redocs/', SpectacularRedocView.as_view(url_name='schemahaha'), name='redocs'),  # Swagger UI
    path('api/hello/', HelloWorldView.as_view(), name='hello-world'),
    path('api/echo/', EchoView.as_view(), name='echoooo'),
    path('api/example/', ExampleView.as_view(), name='echoooo'),
]
