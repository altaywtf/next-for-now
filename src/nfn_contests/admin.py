from django.contrib import admin

from .models import Contest

class ContestAdmin(admin.ModelAdmin):
	list_display = ('title', 'owner', 'category', 'date_started', 'date_deadline')

admin.site.register(Contest, ContestAdmin)