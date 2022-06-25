from django.shortcuts import render

from django.views import generic

# Create your views here.

class PostListView(generic.ListView):
    model = Post

class PostCreateView(generic.CreateView):
    model = Post    
    fields = “__all__”
    success_url  = reverse_lazy(“blog:all”)

class PostDetailView(generic.DetailView):
    model = Post    
  
class PostUpdateView(generic.UpdateView):
    model = Post
    fields = “__all__”
    success_url  = reverse_lazy(“blog:all”)    

class PostDeleteView(generic.DeleteView):   # (generic.UpdateView) in the manual
    model = Post
    fields = “__all__”
    success_url  = reverse_lazy(“blog:all”)
  
