from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

from blog.forms import RegisterForm, LoginForm, CommentForm, ArticleForm
from blog.models import Article, Comment
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView


# Create your views here.

# def index(request):
#     articles = Article.objects.filter(publish=True)
#     context = {
#         "title":"News",
#         "articles":articles
#     }
#     return render(request, "blog/index.html", context)

class ArticleView(ListView):
    model = Article
    template_name = "blog/index.html"
    context_object_name = "articles"
    extra_context = {
        "title":"Article List"
    }

    def get_queryset(self):
        data = Article.objects.filter(publish=True)
        return data

# def get_articles_category(request,pk):
#     articles = Article.objects.filter(category_id=pk,publish=True)
#     context = {
#         "title": "News",
#         "articles":articles
#     }
#     return render(request, "blog/index.html", context)

class ArticleByCategory(ArticleView):
    def get_queryset(self):
        return Article.objects.filter(category_id=self.kwargs["pk"],publish=True)

# def article_detail(request, pk):
#     article = Article.objects.get(pk=pk)
#     comment_form = CommentForm()
#     comments = Comment.objects.filter(article=article)
#     context = {
#         'title':article.title,
#         "article":article,
#         "comment_form":comment_form,
#         "comments":comments
#     }
#     return render(request, "blog/detail.html", context)

class ArticleDetail(DetailView):
    model = Article
    context_object_name = "article"
    template_name = "blog/detail.html"

    def get_queryset(self):
        return Article.objects.filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        article = Article.objects.get(pk=self.kwargs['pk'])
        context['comments'] = Comment.objects.filter(article=article)
        context['comment_form'] = CommentForm()
        return context


def register(request):
    if request.method == "POST":
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("login")
    else:
        form = RegisterForm()
    context = {
        "title":"Register",
        'form':form
    }
    return render(request,'blog/register.html', context)

def user_login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("index")
    else:
        form = LoginForm()
    context = {
        "title":"Login",
        'form':form
    }
    return render(request,'blog/login.html', context)

def user_logout(request):
    logout(request)
    return redirect("index")


def profile(request):
    context = {
        "title":"Profile"
    }
    return render(request, 'blog/profile.html', context)


def save_comment(request,article_id):
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.article = Article.objects.get(pk=article_id)
        comment.save()
    else:
        pass

    return redirect('detail', article_id)

class AddArticle(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "blog/add_article.html"
    extra_context = {
        "title":"Add Article"
    }

class EditArticle(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = "blog/add_article.html"
    extra_context = {
        "title": "Edit Article"
    }

class DeleteArticle(DeleteView):
    model = Article
    form_class = ArticleForm
    template_name = "blog/add_article.html"
    extra_context = {
        "title": "Delete Article"
    }
    success_url = reverse_lazy('index')

