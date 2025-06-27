from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import User, Pop

from .forms import PopForm

class Mailgb(TemplateView):
    template_name = "det.html"

class UserList(ListView):
    model = Pop
    context_object_name = "users"
    template_name = 'index.html'

class UserDetail(DetailView):
     model = Pop
     context_object_name = "users"
     template_name = "index2.html"

class CreateUser(CreateView):
    form_class = PopForm
    success_url = reverse_lazy("user")
    template_name= 'jop.html'

class PopListView(ListView):
    model = Pop
    context_object_name = "Popo"
    template_name = 'jop.html'