from django.shortcuts import render

# Create your views here.

def blog_home(request):
    return render(request, 'blog/home.html')

def post_detail(request, post_id):
    return render(request, 'blog/post_detail.html', {'post_id': post_id})

def category_posts(request, category):
    return render(request, 'blog/category_posts.html', {'category': category})

def author_posts(request, author):
    return render(request, 'blog/author_posts.html', {'author': author})
