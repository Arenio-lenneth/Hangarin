from django.contrib import admin

from .models import Task, Substask, Category, Priority, Note

class SubTaskInline(admin.TabularInline):
    model = SubTask
    extra = 1
    fields = ("title", "status")
    show_change_link = True
class NoteInline(admin.StackedInline):
    model = Note
    extra = 1
    fields = ("content", "created_at")
    readonly_fields = ("created_at",)

class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "deadline", "priority", "category")
    list_filter = ("status", "priority", "category")
    search_field = ("title", "description")

class SubTaskAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "parent_task")
    list_filter = ("status",)
    search_field = ("title",)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_field = ("name",)

class PriorityAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_field = ("name",)

class NoteAdmin(admin.ModelAdmin):
    list_display = ("content", "task", "created_at")
    list_filter = ("created_at",)
    search_field = ("content",)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "deadline", "priority", "category")
    list_filter = ("status", "priority", "category")
    search_fields = ("title", "description")
    inlines = [SubTaskInline, NoteInline]

admin.site.register(Task, TaskAdmin)
admin.site.register(Substask, SubTaskAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Priority, PriorityAdmin)
admin.site.register(Note, NoteAdmin)
