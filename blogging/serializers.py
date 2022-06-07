"""
Title:      serializers.py

Addon #3: Django Rest Framework

Django REST Framework will also make a cool web API that you can visit. For
example, check out http://fierce-crag-38242.herokuapp.com/api/

The tutorial: https://www.django-rest-framework.org/tutorial/quickstart/

The extra instructions:

    After `pip install djangorestframework`, be sure to
    `pip freeze > requirements.txt`. You'll need to commit the
    `requirements.txt` so that it's in your pull request.

    The tutorial shows you how to construct API collections for User and Group,
    but you'll want to adapt the instructions to construct API collections for
    User, Post, and Category

    I accomplished this by creating a `blogging/serializers.py` and editing
    `blogging/views.py` and `mysite/urls.py`, as well as `mysite/settings.py`.
    I prepended "api" to the router path in mysite/urls.py:

    For demonstration purposes, I used the
    `permissions.IsAuthenticatedOrReadOnly` permission class, which lets you
    browse your data even if you aren't logged in. Eg:
"""
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Post, Category


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email"]


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = [
            "url",
            "title",
            "text",
            "author",
            "created_date",
            "modified_date",
            "published_date",
        ]


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ["url", "name", "description", "posts"]
