from django.contrib import admin
from log.models import Camera, Lens, Film, Exposure

admin.site.register(Camera)
admin.site.register(Lens)
admin.site.register(Film)
admin.site.register(Exposure)