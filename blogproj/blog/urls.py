from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView


urlpatterns = [
    path('', views.home, name="blog-home"),
    path('about/', views.about, name="blog-about")
]
