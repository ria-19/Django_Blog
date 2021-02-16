from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import BlogPost
from .forms import BlogPostForm

# Create your views here.
def index(request):
    """The home page for learning log."""
    return render(request, 'blogs/index.html')

def topics(request):
    """Shows all topics."""
    topics = BlogPost.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'blogs/topics.html', context)

def topic(request, topic_id):
    """Show a detailed page of a topic."""
    topic= BlogPost.objects.get(id=topic_id)
    details = topic.details
    date_added = topic.date_added
    context = {'topic': topic, 'details': details, 'date_added': date_added}
    return render(request, 'blogs/topic.html', context)

@login_required
def new_topic(request):
    """Add a new blog."""
    if request.method != 'POST':
        #No data submitted; create a blank form.
        form = BlogPostForm()
    else:
        #POST data submitted; process data.
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('blogs:topics')

    #Display a blank or in valid form
    context = {'form': form}
    return render(request, 'blogs/new_topic.html', context)

@login_required
def edit_entry(request, topic_id):
    """Edit exisitng post."""
    topic = BlogPost.objects.get(id=topic_id)
    if topic.owner != request.user:
                raise Http404

    if request.method != 'POST':
        #Initial request; pre-fill form with current entry.
        form = BlogPostForm(instance=topic)
    else:
        #POST data submitted; process data.
        form = BlogPostForm(instance=topic, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:topic', topic_id=topic.id)

    context = {'topic': topic, 'form': form}
    return render(request, 'blogs/edit_entry.html', context)