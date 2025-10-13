from django.views.generic.list import ListView
from hangarin_project.hangarinorg.models import Substask, Priority

class HomePageView(ListView):
    model = Substask
    context_object_name = 'home'
    template_name = "home.html"



# Create your views here.
