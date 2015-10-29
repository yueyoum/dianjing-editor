from django.contrib import admin
from apps.task.models import TaskType, Task, TaskStatus, RandomEvent, RandomEventDialogAfter, RandomEventDialogBefore
# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'level', 'des', 'tp', 'num', 'reward',
                    'client_task', 'success_rate',
                    )

@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'des')


@admin.register(TaskStatus)
class TaskStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon')


class EventDialogBeforeInLine(admin.TabularInline):
    model = RandomEventDialogBefore

class EventDialogAfterInLine(admin.TabularInline):
    model = RandomEventDialogAfter


@admin.register(RandomEvent)
class RandomEventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon', 'level_min', 'level_max', 'trig_name', 'package')
    inlines = [EventDialogBeforeInLine, EventDialogAfterInLine]
