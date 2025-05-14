from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'app/index.html')

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