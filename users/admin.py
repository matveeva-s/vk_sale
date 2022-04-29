from django.contrib import admin
from users.models import User


class UserAdmin(admin.ModelAdmin):
    search_fields = ('username', 'last_name', 'first_name')
    model = User


admin.site.register(User, UserAdmin)
