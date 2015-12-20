from django.contrib import admin

from .models import Category, Contest, Submission

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('pk', 'name', 'slug', 'hex_code', 'hex_code_2')

class ContestAdmin(admin.ModelAdmin):
	list_display = ('pk', 'title', 'slug', 'owner', 'category', 'date_started', 'date_deadline', 'is_ongoing')

class SubmissionAdmin(admin.ModelAdmin):
	list_display = ('pk', 'contest', 'a_names', 'date_posted')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Contest, ContestAdmin)
admin.site.register(Submission, SubmissionAdmin)