from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'role', 'bio')
    search_fields = ('bio',)
    empty_value_display = '-пусто-'
