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
    """A simplified version of our list_view using a render shortcut"""
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('-published_date')

    # template = loader.get_template('blogging/list.html')
    context = {'posts': posts}
    # body = template.render(context)
    # return HttpResponse(body, content_type="text/html")
    return render(request, 'blogging/list.html', context)
    # syntax for render: render(request, template[, ctx][, ctx_instance])


def detail_view(request, post_id):
    """Accepts a view request and returns a response, based on post_id route"""
    # query for published post where published_date is not 'None'
    published = Post.objects.exclude(published_date__exact=None)

    # from the query, find a post that matches the post_id
    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404

    # if the post does exist, push the post to render
    context = {'post': post}

    # Django includes the render function, which does the following things:
    # template - Loading a template
    # context - Creating a context
    # body - Generating a page body using the template & context
    # return - Making an HTTP response from the body
    return render(request, 'blogging/detail.html', context)

