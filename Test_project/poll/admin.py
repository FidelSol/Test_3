from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.forms import UserChangeForm
from django.utils.translation import ugettext_lazy as _
from .models import Personal, Photo, Tests, CustomUser


class CustomUserChangeForm(UserChangeForm):
    u"""Обеспечивает правильный функционал для поля с паролем и показ полей профиля."""
    password = ReadOnlyPasswordHashField(
        label=_("Password"),
        help_text=_("Raw passwords are not stored, so there is no way to see "
                    "this user's password, but you can change the password "
                    "using <a href=\"password/\">this form</a>."))

    def clean_password(self):
        return self.initial["password"]

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'role')


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    list_display = ('username', 'last_name', 'first_name',
                    'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': (
                'first_name', 'last_name', 'email', 'role'
            )}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Groups'), {'fields': ('groups',)}),
    )


# Register your models here.

class PersonalAdmin(admin.ModelAdmin):
    list_display = ('personal_id', 'ext_id', 'full_name')
    list_display_links = ('personal_id', 'ext_id', 'full_name')
    search_fields = ('personal_id', 'ext_id', 'full_name')

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('photo_id', 'personal', 'data_pub', 'data_photo')
    list_display_links = ('photo_id', 'personal', 'data_pub', 'data_photo')
    search_fields = ('photo_id', 'personal', 'data_pub', 'data_photo')

class TestsAdmin(admin.ModelAdmin):
    list_display = ('tests_id', 'personal', 'expected_time', 'result_time')
    list_display_links = ('tests_id', 'personal', 'expected_time', 'result_time')
    search_fields = ('tests_id', 'personal', 'expected_time', 'result_time')



admin.site.register(Personal, PersonalAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Tests, TestsAdmin)
admin.site.unregister(User)
admin.site.register(CustomUser, CustomUserAdmin)


