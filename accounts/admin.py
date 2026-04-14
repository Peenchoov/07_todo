from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm, UserChangeForm
from .models import MyUser


class MyUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = MyUser
    list_display = [
        "username",
        "email",
        "age",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("age",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("age",)}),)


admin.site.register(MyUser, MyUserAdmin)
