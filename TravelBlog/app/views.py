from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from .models import Blog, Comment
from .forms import LoginForm, SignUpForm, BlogForm, CommentForm

# Create your views here.
def home(request):
    blogs = Blog.objects.all().order_by('-date')
    return render(request, 'app/index.html', {'blogs': blogs})

def category(request):
    return render(request, 'app/category.html')

def contact(request):
    return render(request, 'app/contact.html')

def archive(request):
    return render(request, 'app/archive.html')

def elements(request):
    return render(request, 'app/elements.html')

def singleblog(request):
    return render(request, 'app/single-blog.html')

def login_view(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('home')  
    else:
        form = LoginForm()
    return render(request, 'userauth/login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'userauth/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogForm()
    return render(request, 'app/add.html', {'form': form})

def blog_detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    comments = blog.comments.order_by('-created_at')

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user
                comment.blog = blog
                comment.save()
                return redirect('blog_detail', blog_id=blog.id)
        else:
            return redirect('login')
    else:
        form = CommentForm()

    return render(request, 'app/blog_detail.html', {
        'blog': blog,
        'comments': comments,
        'form': form
    })