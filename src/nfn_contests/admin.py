from django.contrib import admin

from .models import Contest, Submission

class ContestAdmin(admin.ModelAdmin):
	list_display = ('pk', 'title', 'owner', 'category', 'date_started', 'date_deadline')

class SubmissionAdmin(admin.ModelAdmin):
	list_display = ('pk', 'contest', 'a_names', 'date_posted')

admin.site.register(Contest, ContestAdmin)
admin.site.register(Submission, SubmissionAdmin)