from django.contrib import admin
from .models import Note

# Register your models here.
class NoteDetails(admin.ModelAdmin):
    pass
admin.site.register(Note, NoteDetails)