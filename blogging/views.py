from django.http.response import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from blogging.models import Post


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


def stub_view(request, *args, **kwargs):
    """A default view that can be used as a placeholder"""
    body = "Stub View\n\n"
    if args:
        body += "Args: \n"

        # for each argument in args, add a tab for each argument
        body += "\n".join(["\t%s" % a for a in args])

    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" % k for k in kwargs.items()])

    return HttpResponse(body, content_type="text/plain")
