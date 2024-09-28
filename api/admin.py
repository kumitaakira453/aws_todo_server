from django.contrib import admin

from .models import Todo


# Register your models here.
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "detail", "deadLine", "is_done", "is_deleted"]
    list_editable = ["title", "deadLine", "is_done", "is_deleted"]
