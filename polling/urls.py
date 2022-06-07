"""
Title:      urls.py
"""
from django.urls import path
from polling.views import PollListView, PollDetailView

#  from polling.views import ListView, DetailView

urlpatterns = [
    # path('', list_view, name="poll_index"),  # old list view
    # path('polls/<int:poll_id>/', detail_view, name="poll_detail"),
    # we use PollListView() because we need to create a new instance
    # path('', PollListView().as_view(), name="poll_index"),  # for custom
    # path('polls/<int:poll_id>', detail_view, name="poll_detail"),
    path("", PollListView.as_view(), name="poll_index"),  # for built-in
    path("polls/<int:pk>", PollDetailView.as_view(), name="poll_detail"),
]
