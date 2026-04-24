from django.contrib import admin
from django.urls import path

from app import views
from app.api import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
    path('', views.render_homepage, name='homepage'),
    path('about/', views.render_about, name='about'),
]
