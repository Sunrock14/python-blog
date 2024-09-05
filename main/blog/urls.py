from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('category/<str:category>/', views.category_posts, name='category_posts'),
    path('author/<str:author>/', views.author_posts, name='author_posts'),
]