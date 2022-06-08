"""
Title:      models.py
"""
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from datetime import datetime


class Post(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(
        auto_now_add=True,
    )
    modified_date = models.DateTimeField(
        auto_now=True,
    )
    published_date = models.DateTimeField(
        blank=True,
        null=True,
        auto_now_add=True,
    )

    def __str__(self):
        return self.title

    @staticmethod
    def get_absolute_url():
        return reverse("blog_index")


class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    posts = models.ManyToManyField(Post, blank=True, related_name="categories")

    def __str__(self) -> str:
        return self.name

    @staticmethod
    def get_absolute_url():
        return reverse("blog_index")

    class Meta:
        # fixes the plural spelling of 'Categories' within Django
        verbose_name_plural = "Categories"
