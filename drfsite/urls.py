"""drfsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from main.views import *
from rest_framework import routers


# router = routers.SimpleRouter()

router = routers.DefaultRouter()
router.register(r'article', ArticleViewSet, basename='article')


urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls))

    # path('api/v1/articlelist/', ArticleViewSet.as_view({'get': 'list'})),
    # path('api/v1/articlelist/<int:pk>/', ArticleViewSet.as_view({'put': 'update'})),

    # path('api/v1/articlelist/', ArticleAPIList.as_view()),
    # path('api/v1/articlelist/<int:pk>/', ArticleAPIUpdate.as_view()),
    # path('api/v1/articledetail/<int:pk>/', ArticleAPIDetailView.as_view()),

]
