from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView


urlpatterns = [
    path('about/', views.about, name="blog-about")
    path('', PostListView.as_view(), name="blog-home"),

    
]

