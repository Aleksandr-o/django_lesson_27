from django.contrib import admin
from apps.todo.models import (Task,
    Category,
    Status,
    SubTask
    )

#Advance registration.
@admin.register(Task)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'creator', 'created_at')
    list_filter = ('category', 'status', 'creator', 'created_at')
    search_fields = ('title',)

@admin.register(SubTask)
class ModelNameAdmin(admin.ModelAdmin):
    def change_subtasks_register(self, request, queryset):
        for obj in queryset:
            obj.title = obj.title.upper()
            obj.save()

    change_subtasks_register.short_description = "Up register"

    actions = ['change_subtasks_register']
    list_display = ('title', 'category', 'task', 'status', 'creator', 'created_at')
    list_filter = ('task', 'category', 'status', 'creator', 'created_at')
    search_fields = ('title',)

@admin.register(Status)
class ModelNameAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class ModelNameAdmin(admin.ModelAdmin):
    pass
