from django.urls import path
from .views import home, category, contact, elements, archive, singleblog, login_view, signup_view, logout_view, add_blog, blog_detail


urlpatterns = [
    path('', home, name="home"),
    path('category/', category, name='category'),
    path('contact/', contact, name='contact'),
    path('elements/', elements, name='elements'),
    path('archive/', archive, name='archive'),
    path('singleblog/', singleblog, name='singleblog'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('add/', add_blog, name='add_blog'),
    path('blog/<int:blog_id>/', blog_detail, name='blog_detail'),
]