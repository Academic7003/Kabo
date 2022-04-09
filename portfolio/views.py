from dataclasses import fields
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from portfolio.models import PortfolioModel



class PortfolioView(ListView):
    template_name ='portfolio.html'
    model = PortfolioModel
    context_object_name = 'portfolio_list'


class PortfolioDetail(DetailView):
    model = PortfolioModel
    context_object_name = 'portfolio'
    template_name = 'detail-portfolio.html'


class PortfolioUpdate(UpdateView):
    model = PortfolioModel
    fields = ['title','body', 'image']
    template_name = 'update-portfolio.html'

class PortfolioCreate(CreateView):
    model = PortfolioModel
    template_name = 'create-portfolio.html'
    fields = ['title', 'body', 'image']

class PortfolioDelete(DeleteView):
    model = PortfolioModel
    template_name = 'delete-portfolio.html'
    success_url = reverse_lazy('portfolio:main-portfolio')
    context_object_name = 'portfolio'