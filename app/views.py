from django.urls import reverse_lazy
from app.models import Article
from django.shortcuts import render 
from django.views.generic import CreateView,ListView, DeleteView, UpdateView


class ArticleListView(ListView):
    template_name = 'app/home.html'
    model = Article
    context_object_name = 'articles'

class ArticleCreateView(CreateView):
    template_name = 'app/create_article.html'
    model = Article
    fields = ['title', 'status', 'content', 'twitter_post']
    success_url = reverse_lazy('home')

class ArticleUpdateView(UpdateView):
    template_name = 'app/update_article.html'
    model = Article
    fields = ['title', 'status', 'content', 'twitter_post']
    success_url = reverse_lazy('home')
    context_object_name = 'article'

class ArticleDeleteView(DeleteView):
    template_name = 'app/delete_article.html'
    model = Article
    success_url = reverse_lazy('home')
    context_object_name = 'article'