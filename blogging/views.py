from django.shortcuts import render
from django.http.response import HttpResponse, Http404
from django.template import loader

from blogging.models import Post


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


'''
def list_view(request):
    """The more manual setup of a list_view, lists posts"""
    published = Post.objects.exclude(published_date__exact=None)

    # shows the newest first (you have to reverse published date)
    posts = published.order_by('-published_date')

    # loader lets us load an HTML template
    template = loader.get_template('blogging/list.html')

    context = {'posts': posts}
    body = template.render(context)
    return HttpResponse(body, content_type="text/html")
'''


def list_view(request):
    """A simplified version of our list_view"""
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('-published_date')

    # template = loader.get_template('blogging/list.html')
    context = {'posts': posts}
    # body = template.render(context)
    # return HttpResponse(body, content_type="text/html")
    return render(request, 'blogging/list.html', context)


def detail_view(request, post_id):
    published = Post.objects.exclude(published_date__exact=None)

    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404

    context = {'post': post}
    return render(request, 'blogging/detail.html', context)

