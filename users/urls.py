from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register('', views.UsersView, 'users')
urlpatterns = [
    path('', include(router.urls)),
    path('auth/login/', views.CreateTokenView.as_view())
]
