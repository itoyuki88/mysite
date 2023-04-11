from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Post

#def view1(request):
#    return HttpResponse("<h1>View 1</h1><h2>view 1</h2><p>test</p>")

def tempview(request):
    return render(request, template_name="blog/test.html")

def chiview(request):
    return render(request, template_name="blog/chikawa.html")

class PostListView(ListView):
    model = Post
    template_name = "blog/test2.html"


