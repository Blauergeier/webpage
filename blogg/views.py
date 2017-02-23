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

    blog_list = Blog.objects.all()
    if blog_list.count():
        button_size = 100.00 / blog_list.count()
    else:
        button_size = 100

    context = {
        'latest_entries' : entries,
        'blog_list' : blog_list,
        'button_size' : button_size,
    }
    return render(request, 'blogg/index.html', context)

def detail(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    return render(request, 'blogg/detail.html', {'entry': entry})

