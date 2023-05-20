from rest_framework import routers
from django.urls import path, include
from .views import PostView, CommentView, CategoryView

router = routers.DefaultRouter()
router.register('posts', PostView, 'posts')
router.register('comments', CommentView, 'comments')
router.register('categories', CategoryView, 'categories')

urlpatterns = [
    path('', include(router.urls))
]
