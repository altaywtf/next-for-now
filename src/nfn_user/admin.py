from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from nfn_user.models import C_Owner

class C_OwnerInline(admin.StackedInline):
	model = C_Owner
	can_delete = False
	verbose_name_plural = 'Contest Owner'

class UserAdmin(BaseUserAdmin):

	#Inlines fields according to user group in 'Change View'
	def change_view(self, request, object_id, form_url='', extra_context=None):
		user = User.objects.get(pk=object_id)
		current_inlines = []
		if user.groups.all().count() > 0:
			for index in range(len(user.groups.all())):
				if user.groups.all()[0].name == 'Contest Owner':
					current_inlines.append(C_OwnerInline)
		self.inlines = current_inlines
		return super(UserAdmin, self).change_view(request, object_id, form_url, extra_context=extra_context)

	#Modifies "Add View"
	def add_view(self, request, form_url='', extra_context=None):
		return super(UserAdmin, self).add_view(request)

	

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
#admin.site.register(C_Owner)
