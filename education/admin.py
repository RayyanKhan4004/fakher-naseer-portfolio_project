from django.contrib import admin
from .models import Education


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree_title', 'institution', 'duration', 'score', 'order')
    list_editable = ('order',)
