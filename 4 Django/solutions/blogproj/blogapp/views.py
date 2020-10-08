from django.shortcuts import render

from .models import BlogPost, Comment

def index(request):
    posts = BlogPost.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blogapp/index.html', context)

def detail(request, blog_post_id):
    post = BlogPost.objects.get(id=blog_post_id)
    top_level_comments = post.comments.all()
    # top_level_comments = post.comments.filter(parent__isnull=True)
    context = {
        'post': post,
        'top_level_comments': top_level_comments
    }
    return render(request, 'blogapp/detail.html', context)