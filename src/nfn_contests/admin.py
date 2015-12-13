from django.contrib import admin

from .models import Contest

class ContestAdmin(admin.ModelAdmin):
	list_display = ('title', 'category')
	search_field = ('title')

admin.site.register(Contest, ContestAdmin)