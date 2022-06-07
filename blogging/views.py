"""
Title:      views.py
"""
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, PostSerializer, CategorySerializer

from blogging.models import Post, Category


class BlogListView(ListView):
    """A view inheriting from Django's generic ListView"""

    queryset = Post.objects.exclude(published_date__exact=None).order_by(
        "-published_date"
    )
    template_name = "blogging/list.html"


class BlogDetailView(DetailView):
    """A view inheriting from Django's generic DetailView"""

    queryset = Post.objects.exclude(published_date__exact=None)
    template_name = "blogging/detail.html"


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
