from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import ProfileUserCreationForm, ProfileUserChangeForm
from .models import ProfileUser

class ProfileUserAdmin(UserAdmin):
	add_form = ProfileUserCreationForm
	form = ProfileUserChangeForm
	model = ProfileUser
	list_display = ['email', 'username', 'data_nascimento', ]
	fieldsets = UserAdmin.fieldsets + (
		('Campos Customizados', {'fields' : ('data_nascimento', )}),
		)

admin.site.register(ProfileUser, ProfileUserAdmin)	