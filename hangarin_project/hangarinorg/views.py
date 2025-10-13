from django.shortcuts import render
from django.views.generic.list import ListView
from hangarinorg.models import Substask

class HomePageView(ListView):
    model = Substask
    context_object_name = 'home'
    template_name = "home.html"


# Create your views here.
