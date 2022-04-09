from dataclasses import fields
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from news.models import NewsModel
from django.urls import reverse_lazy

class NewsView(ListView):
    model = NewsModel
    context_object_name = 'new'
    template_name = 'news.html'


class NewsDetail(DetailView):
    model = NewsModel
    context_object_name = 'new'
    template_name = 'detail.html'


class NewsUpdate(UpdateView):
    model = NewsModel
    fields = ['title','body', 'image']
    template_name = 'update.html'

class NewsCreate(CreateView):
    model = NewsModel
    template_name = 'create.html'
    fields = ['title', 'body', 'author', 'image']

class NewsDelete(DeleteView):
    model = NewsModel
    template_name = 'delete.html'
    success_url = reverse_lazy('news:news-page')
    context_object_name = 'new'