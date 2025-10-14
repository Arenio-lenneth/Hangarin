from hangarin_project.hangarinorg.models import Task, Substask, Category, Priority, Note
from hangarin_project.hangarinorg.forms import TaskForm, SubTaskForm, CategoryForm, PriorityForm, NoteForm
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class HomePageView(ListView):
    model = Task
    context_object_name = 'home'
    template_name = "home.html"

#Listviews
class TaskList(ListView):
    model = Task
    context_object_name = 'task'
    template_name = 'task_list.html'
    paginate_by = 5

class SubtaskList(ListView):
    model = Substask
    context_object_name = 'subtask'
    template_name = 'subtask_list.html'
    paginate_by = 5

class CategoryList(ListView):
    model = Category
    context_object_name = 'category'
    template_name = 'category_list.html'
    paginate_by = 5

class PriorityList(ListView):
    model = Priority
    context_object_name = 'priority'
    template_name = 'priority_list.html'
    paginate_by = 5

class NoteList(ListView):
    model = Note
    context_object_name = 'note'
    template_name = 'note_list.html'
    paginate_by = 5

#CreateViews
class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task form.html'
    success_url = reverse_lazy('task-list')

class SubtaskCreateView(CreateView):
    model = Substask
    form_class = SubTaskForm
    template_name = 'subtask form.html'
    success_url = reverse_lazy('subtask-list')

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category form.html'
    success_url = reverse_lazy('category-list')

class PriorityCreateView(CreateView):
    model = Priority
    form_class = PriorityForm
    template_name = 'priority form.html'
    success_url = reverse_lazy('priority-list')

class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'note form.html'
    success_url = reverse_lazy('note-list')

#UpdateViews
class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task-list')

class SubtaskUpdateView(UpdateView):
    model = Task
    form_class = SubTaskForm
    template_name = 'subtask_form.html'
    success_url = reverse_lazy('subtask-list')

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category-list')

class PriorityUpdateView(UpdateView):
    model = Priority
    form_class = PriorityForm
    template_name = 'priority_form.html'
    success_url = reverse_lazy('priority-list')

class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'
    success_url = reverse_lazy('note-list')

#DeleteViews
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_del.html'
    success_url = reverse_lazy('task-list')

class SubtaskDeleteView(DeleteView):
    model = Substask
    template_name = 'subtask_del.html'
    success_url = reverse_lazy('subtask-list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category_del.html'
    success_url = reverse_lazy('category-list')

class PriorityDeleteView(DeleteView):
    model = Priority
    template_name = 'priority_del.html'
    success_url = reverse_lazy('priority-list')

class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'note_del.html'
    success_url = reverse_lazy('note-list')





# Create your views here.
