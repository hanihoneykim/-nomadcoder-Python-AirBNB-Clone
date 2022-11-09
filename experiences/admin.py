from django.contrib import admin
from .models import Experience, Perk


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("name", "start", "end")
    list_filter = ("start", "category")


@admin.register(Perk)
class PertAdmin(admin.ModelAdmin):
    list_display = ("name", "detail", "explanation")
