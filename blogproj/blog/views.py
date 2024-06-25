from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView






posts = [
    {
        'author': 'Destiny Franks',
        'title': 'Blog Post 1',
        'content': 'This is my first blog post',
        'date_posted': '7th May, 2024'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'This is my second blog post',
        'date_posted': '14th May, 2024'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': "About Page"})
