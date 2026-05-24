from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # 1. Django 內建的後台
    path('admin/', admin.site.urls),
    
    # 2. 將所有根網址交給 library 處理
    path('', include('library.urls')), 
]