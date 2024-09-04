# /blog_project/djangoapp/blog/urls.py

from django.urls import path
from blog.views import index # /blog_project/djangoapp/blog/views.py

app_name = 'blog'
urlpatterns = [
    path('', index, name='index'),
]