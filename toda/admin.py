from django.contrib import admin
from toda.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('task','is_completed','updated_at','created_at') # display admin page
    search_fields = ('task',)

admin.site.register(Task,TaskAdmin)

# Register your models here.



