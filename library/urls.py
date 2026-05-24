from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView
from .views import BookViewSet, BorrowRecordViewSet, ChatbotView 

# 設定 API 路由
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
router.register(r'records', BorrowRecordViewSet, basename='record')

urlpatterns = [
    # 讀者前台網址
    path('', TemplateView.as_view(template_name='user.html'), name='user_index'),
    
    # 管理員後台網址
    path('library-admin/', TemplateView.as_view(template_name='admin.html'), name='admin_index'),
    
    # 提供給前端的 API 網址
    path('api/', include(router.urls)),
    path('api/chatbot/', ChatbotView.as_view(), name='chatbot'),
]