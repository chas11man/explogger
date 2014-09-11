from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.models import User
from log.models import Camera, Lens, Film, Exposure, UserProfile


class UserInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = ''


class UserAdmin(DjangoUserAdmin):
    inlines = (UserInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Camera)
admin.site.register(Lens)
admin.site.register(Film)
admin.site.register(Exposure)