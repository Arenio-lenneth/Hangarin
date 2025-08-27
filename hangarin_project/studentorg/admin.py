from django.contrib import admin

from .models import Task, Substask, Category, Note, Priority

admin.site.register(Task)
admin.site.register(Substask)
admin.site.register(Category)
admin.site.register(Note)
admin.site.register(Priority)
