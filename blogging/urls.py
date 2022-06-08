from django.urls import path
from blogging.views import (
    BlogListView,
    BlogDetailView,
    AddPostView,
    UpdatePostView,
    DeletePostView,
)

from .rss import LatestEntriesFeed

# a list of routes
urlpatterns = [
    path("", BlogListView.as_view(), name="blog_index"),
    path("posts/<int:pk>", BlogDetailView.as_view(), name="blog_detail"),
    path("latest/feed/", LatestEntriesFeed()),
    path("add/", AddPostView.as_view(), name="add_post"),
    path("update/<int:pk>", UpdatePostView.as_view(), name="update_post"),
    path("delete/<int:pk>", DeletePostView.as_view(), name="delete_post"),
]
