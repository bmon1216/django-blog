"""
Title:      rss.py

Addon #4: Fancy RSS Feed

The end result: Your blog now has a fancy RSS feed. If users have an RSS feed
reader then they can subscribe to your feed and automatically receive updates e
very time you make a new post.

The tutorial:
https://docs.djangoproject.com/en/2.2/ref/contrib/syndication/#a-simple-example

The extra instructions:

    You'll have to adapt this example to use the `Post` model instead of the
    made-up `NewsItem` model.

    In the `item_title` and `item_description` methods, the `item` variable
    that gets passed in will be an instance of `Post`: you may have to adapt
    those methods.

    The part of this that usually trips students up is the `item_link` method.
    Basically for any given Post (item), you need to provide a URL for the
    detail view of that post.
    Well, we don't have a "news-item" view, but we do
    have a similar view that you can find inside `blogging/urls.py`.

    To accomplish this add-on, I had to edit `blogging/views.py`
    and `blogging/urls.py`.
"""
from django.contrib.syndication.views import Feed
from django.urls import reverse

from .models import Post


class LatestEntriesFeed(Feed):
    title = "VideoGame, Tech, and Python News"
    link = "/sitenews/"
    description = "Updates on all the latest VG, Tech, and Python news"

    def items(self):
        return Post.objects.order_by("-published_date")[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text

    # item_link is only needed if Post has no get_absolute_url method.
    def item_link(self, item):
        return reverse("blog_detail", args=[item.pk])
