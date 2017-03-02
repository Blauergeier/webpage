from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone

from .models import Entry, Blog

# Create your views here.


def index(request, blog_name=None): #Default page currently has no name
    if blog_name:
        entries = Entry.objects.filter(blog__topic=blog_name).filter(pub_date__lte=timezone.now()).order_by('pub_date')[:5]
    else:
        entries = Entry.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')[:5]

    button_size = __calculate_button_size()

    context = {
        'latest_entries' : entries,
        'blog_list' : Blog.objects.all(),
        'button_size' : button_size,
    }
    return render(request, 'blogg/index.html', context)


def detail(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    split_result = entry.content.splitlines()

    button_size = __calculate_button_size();

    context = {
        'content': split_result,
        'entry_title': entry.titel,
        'blog_list': Blog.objects.all(),
        'button_size': button_size,
    }

    return render(request, 'blogg/detail.html', context)


# #The calculation of the button size will be done multiple times in order to track changes on the website
# #Private to hide it from the url script
def __calculate_button_size():
    blog_list = Blog.objects.all()
    if blog_list.count():
        button_size = 100.00 / blog_list.count()
    else:
        button_size = 100

    return button_size


