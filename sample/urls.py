from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


app_name = 'sample'

# router = DefaultRouter()
# router.register(r'posts', views.PostViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('posts/', views.PostListAPIView.as_view()),
]
