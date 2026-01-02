# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Tag
from .forms import CommentForm
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import SearchForm


def home(request):
    post_list = Post.objects.all().order_by('-created_at')

    paginator = Paginator(post_list, 5)  # 5 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/home.html', {
        'page_obj': page_obj
    })



def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug) 
    comments = post.comments.filter(active=True) 
    new_comment = None

    '''
    paginator = Paginator(post_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    '''
    if request.method == 'POST':
        form = CommentForm(request.POST) 
        if form.is_valid():
            new_comment = form.save(commit=False) 
            new_comment.post = post 
            new_comment.save()
        
    else:
        form = CommentForm()
        
    return render(request, 'blog/post_detail.html', { 
            'post': post, 
            'comments': comments, 
            'form': form, 
            'new_comment': new_comment 
            })


def category_posts(request, slug):
    category = Category.objects.get(slug=slug)
    post_list = category.posts.all()

    paginator = Paginator(post_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/category_posts.html', {
        'category': category,
        'page_obj': page_obj
    })



def tag_posts(request, slug):
    tag = Tag.objects.get(slug=slug)
    posts = tag.posts.all()

    '''
    paginator = Paginator(post_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    '''
    return render(request, 'blog/tag_posts.html', {
        'tag': tag,
        'posts': posts
    })



def search(request):
    form = SearchForm()
    query = None
    results = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Post.objects.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query)
            ).order_by('-created_at')

    return render(request, 'blog/search.html', {
        'form': form,
        'query': query,
        'results': results
    })


def category(request):
    category = Category.objects.get(slug=slug)
    post_list = category.posts.all()
    paginator = Paginator(post_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/category_posts.html', {
       'category': category,
       'page_obj': page_obj
    
    })
