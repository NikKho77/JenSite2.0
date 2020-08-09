from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import PostMainPage,PhotoModel

# Create your views here.
class PostMainPageView(ListView):
    model = PostMainPage
    template_name = 'home.html'

class PhotoModelView(ListView):
    model = PhotoModel
    template_name = 'gallery.html'