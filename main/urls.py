from django.urls import path, include

from . import views
from main.views import *

urlpatterns = [
    path('', views.article_view),

]
