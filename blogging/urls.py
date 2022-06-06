from django.urls import path
from blogging.views import BlogListView, BlogDetailView

# a list of routes
urlpatterns = [
    path('', BlogListView.as_view(), name="blog_index", ),
    path('posts/<int:pk>', BlogDetailView.as_view(), name="blog_detail"),
]
