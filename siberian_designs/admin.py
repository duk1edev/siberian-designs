from django.contrib import admin
from .models import Work, Example
# Register your models here.

admin.site.register(Work)
# admin.site.register(Example)

@admin.register(Example)
class ExampleModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'work')
    list_filter = ('work',)