from django.contrib import admin
from .models import *


class IncorrectAdmin(admin.ModelAdmin):
    list_display = ['word', 'correct']
    list_display_links = ['word']


class IncorrectInline(admin.TabularInline):
    model = Incorrect
    extra = 1


class CorrectAdmin(admin.ModelAdmin):
    list_display = ['word']
    list_display_links = ['word']
    inlines = [IncorrectInline]


admin.site.register(Correct, CorrectAdmin)
admin.site.register(Incorrect, IncorrectAdmin)
