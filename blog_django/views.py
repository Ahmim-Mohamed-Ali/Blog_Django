from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.urls import reverse_lazy
# Create your views here.
from .models import Post
from django.contrib.auth.models import User


# def my_view(request):
#     posts=None
#     if request.user.is_authenticated:
#         posts=Post.objects.filter(created_by=request.user)

#     print("Your Posts",posts)
#     return render(request,'blog_django/home.html',context={
#         "posts":posts
#     })


class PostDetailView(DetailView):
    model=Post


class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields = ['title', 'content'] 


    def form_valid(self,form):
        form.instance.created_by=self.request.user
        return super().form_valid(form)
    

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields = ['title', 'content'] 
    template_name = 'blog_django/post_update.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user  # Assigner l'utilisateur connecté
        return super().form_valid(form)
    
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.created_by:
            return True 
        else:
            return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    success_url = reverse_lazy('blog-home')  # Rediriger vers la page d'accueil


    def test_func(self):
        post=self.get_object()
        if self.request.user==post.created_by:
            return True 
        else:
            return False

class PostListView(ListView):
    model=Post
    template_name="blog_django/home.html"
    context_object_name="posts"
    paginate_by=2


class UserPostListView(ListView):
    model=Post
    template_name="blog_django/user_posts.html"
    context_object_name="posts"
    paginate_by=2

    def get_queryset(self):
        self.user = get_object_or_404(User, id=self.kwargs["id_user"])
        return Post.objects.filter(created_by=self.user)




def about(request):
    return render(request,'blog_django/about.html',context={
        "title":"About"
    })
