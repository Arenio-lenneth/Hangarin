from django.forms import ModelForm
from .models import Task, Subtask, Category, Priority, Note

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = "__all__"

class SubTaskForm(ModelForm):
    class Meta:
        model = Subtask
        fields = "__all__"

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

class PriorityForm(ModelForm):
    class Meta:
        model = Priority
        fields = "__all__"

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = "__all__"
