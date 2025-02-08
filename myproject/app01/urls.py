
from .views import Base64Encryption, AESEncryption, CacheView, TaskView
from django.urls import path, include

urlpatterns = [
    path('base64/', Base64Encryption.as_view()),
    path('aes/', AESEncryption.as_view()),
    path('cache/', CacheView.as_view()),
    path('start/tasks/', TaskView.as_view(), name='task-create'),
    path('get/tasks/<str:pk>/', TaskView.as_view(), name='task-result'),

]
