# /blog_project/djangoapp/blog/urls.py

from django.urls import path
from blog.views import index, page, post

app_name = 'blog' ##
# IMPORT⬇: /blog_project/djangoapp/blog/views.py
urlpatterns = [
    path('', index, name='index'), ##
    path('page/', page, name='page'),
    path('post/', post, name='post'),    
]