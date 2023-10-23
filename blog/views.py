from django.shortcuts import render , get_object_or_404
from .models import Blog , Tags , Category , Comments
from .forms import CommentForm
from django.core.paginator import Paginator

# Create your views here.


def blog_list(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 2) 
    page_number = request.GET.get('page')
    blog_list = paginator.get_page(page_number)
    context={
        'blog_list':blog_list,
        
    }
    return render (request , 'blog/blog.html' , context)

def blog_detail(request , id):
    blog = get_object_or_404(Blog , id = id)
    tags = Tags.objects.all().filter(blogs = blog)
    categories = Category.objects.all()
    recents = Blog.objects.all().order_by("-create_at")[:5]
    comments = Comments.objects.all().filter(blog = blog)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data['name']
            new_email = form.cleaned_data['email']
            new_comment= form.cleaned_data['comment']
            
            n_comment = Comments(blog=blog , name=new_name , email=new_email , comment=new_comment)
            n_comment.save()
    
    context = {
        'blog':blog,
        'tags' :tags,
        'categories': categories ,
        'recents' : recents,
        'comments' :comments,
    }
    return render(request , 'blog/blog_detail.html', context)

def blog_tag(request , tag):
    blogs = Blog.objects.filter(tags__slug=tag)
    context={
        'blogs':blogs
        }
    return render (request , 'blog/blog.html' , context)

def blog_category(request , category):
    blogs = Blog.objects.filter(category__slug=category)
    context={
        'blogs':blogs     
    }
    return render (request , 'blog/blog.html' , context)

def search(request):
    if request.method == 'GET':
        srch = request.GET.get("search")
    blog_list = Blog.objects.filter(title__icontains=srch)
    return render(request , 'blog/blog.html' , {'blog_list':blog_list})