from django.contrib import admin
from .models import Skill, Software


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'rating', 'order')
    list_editable = ('rating', 'order')
    list_filter = ('category',)


@admin.register(Software)
class SoftwareAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'status_note', 'order')
    list_editable = ('rating', 'status_note', 'order')
