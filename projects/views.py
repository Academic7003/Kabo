from dataclasses import fields
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from projects.models import ProjectsModel



class ProjectsView(ListView):
    template_name = 'projects-projects.html'
    model = ProjectsModel
    context_object_name = 'projects'


class ProjectsDetail(DetailView):
    model = ProjectsModel
    context_object_name = 'project'
    template_name = 'projects-detail.html'



class ProjectsUpdate(UpdateView):
    model = ProjectsModel
    fields = ['title', 'image']
    template_name = 'projects-update.html'

class ProjectsCreate(CreateView):
    model = ProjectsModel
    template_name = 'projects-create.html'
    fields = ['title','image']

class ProjectsDelete(DeleteView):
    model = ProjectsModel
    template_name = 'projects-delete.html'
    success_url = reverse_lazy('projects:projects')
    context_object_name = 'project'

