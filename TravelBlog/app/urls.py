from django.urls import path
from .views import home, category, contact, elements, archive, singleblog

urlpatterns = [
    path('', home, name="home"),
    path('category/', category, name='category'),
    path('contact/', contact, name='contact'),
    path('elements/', elements, name='elements'),
    path('archive/', archive, name='archive'),
    path('singleblog/', singleblog, name='singleblog'),
]