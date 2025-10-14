from hangarin_project.hangarinorg.models import Task, Substask, Category, Priority, Note
from hangarin_project.hangarinorg.forms import TaskForm
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy


class HomePageView(ListView):
    model = Task
    context_object_name = 'home'
    template_name = "home.html"

class TaskList(ListView):
    model = Task
    context_object_name = 'task'
    template_name = 'task_list.html'
    paginate_by = 5

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task form.html'
    success_url = reverse_lazy('task-list')

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')




# Create your views here.
