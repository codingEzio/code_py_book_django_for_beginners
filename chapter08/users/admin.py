from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
	""" The model & forms are closely connected to here!
	"""
	
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	model = CustomUser
	list_display = ['email', 'username', 'age', 'is_staff', ]


# We've only "registered" a 'model' once before,
#   now we'll add one more thing: `CustomUserAdmin`
admin.site.register(CustomUser, CustomUserAdmin)

# Just a quick note
#   UserAdmin <- models(AbstractUser) -> form <- two-super-forms
