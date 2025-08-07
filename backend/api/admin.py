from multiprocessing.reduction import register

from django.contrib import admin
from .models import Note
# Register your models here.
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Note._meta.fields]
