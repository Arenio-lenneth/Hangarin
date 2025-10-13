from hangarin_project.hangarinorg.models import Substask, Task
from hangarin_project.hangarinorg.forms import TaskForm
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


class HomePageView(ListView):
    model = Substask
    context_object_name = 'home'
    template_name = "home.html"

class TaskList(ListView):
    model = Task
    context_object_name = 'task'
    template_name = 'task_list.html'
    paginate_by = 5

class TaskCreateView(CreateView):
    model = Substask
    form_class = TaskForm
    template_name = 'task form.html'
    success_url = reverse_lazy('task-list')



# Create your views here.
