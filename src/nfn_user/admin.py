from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from nfn_user.models import C_Owner

class C_OwnerInline(admin.StackedInline):
	model = C_Owner
	can_delete = False
	verbose_name_plural = 'Contest Owner'

class UserAdmin(BaseUserAdmin):
	inlines = (C_OwnerInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(C_Owner)
