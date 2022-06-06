# polling/views.py

from django.shortcuts import render
from django.http import Http404
from polling.models import Poll

# import the Django Built-in
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


def detail_view(request, poll_id):
    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404

    if request.method == "POST":
        if request.POST.get("vote") == "Yes":
            poll.score += 1
        else:
            poll.score -= 1
        poll.save()

    context = {"poll": poll}
    return render(request, "polling/detail.html", context)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
"""  obsolete code when using Django Built-In generic view
#  Class View sample where we don't use the Django Built-in class views

def list_view(request):
    context = {'polls': Poll.objects.all()}
    return render(request, 'polling/list.html', context)

class ListView:  # switched to _old so that we can use the Django Built-in
    # A sample custom class view for lists, will not be used in production

    def as_view(self):
        # Returns the 'get' method we have as a function
        return self.get

    def get(self, request):
        # A get view method
        model_list_name = self.model.__name__.lower() + '_list'
        # adding the suffix '_list' is for us to imitate djangos class-view
        context = {model_list_name: self.model.objects.all()}
        return render(request, self.template_name, context)
"""


class PollListView(ListView):
    """A view inheriting from Django's generic ListView"""

    model = Poll
    template_name = "polling/list.html"


class PollDetailView(DetailView):
    """A view inheriting from Django's generic DetailView"""

    model = Poll
    template_name = "polling/detail.html"

    def post(self, request, *args, **kwargs):
        """Handles POST requests for the Polling app"""
        poll = self.get_object()

        if request.POST.get("vote") == "Yes":
            poll.score += 1
        else:
            poll.score -= 1
        poll.save()

        context = {"object": poll}
        return render(request, "polling/detail.html", context)
