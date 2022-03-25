

from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import FormPost
from .models import Group, Post, User


def index(request):
    posts_list = Post.objects.all()
    paginator = Paginator(posts_list, settings.POSTS_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:settings.POSTS_PER_PAGE]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    author = User.objects.get(username=username)
    author_post = Post.objects.filter(author=author).order_by('-pub_date')
    posts_numbers = author_post.count()
    paginator = Paginator(author_post, settings.POSTS_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'author ': author,
        'author_post': author_post,
        'posts_numbers': posts_numbers,

    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = Post.objects.select_related('author', 'group').get(id=post_id)
    post_count = Post.objects.filter(author=post).count()
    post_list = post.author.posts.all()
    context = {
        'post_list': post_list,
        'post': post,
        'post_count': post_count,

    }
    return render(request, 'posts/post_detail.html', context)


def post_create(request):

    if request.method == 'POST':
        form = FormPost(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            form.save()
            return redirect('posts:profile', request.user)
        return render(request, 'posts/post_create.html', {'form': form})
    form = FormPost()
    
    
def post_edit(request, post_id):
    post = get_object_or_404(Post, pk= post_id)
    
    
    
