from django.contrib import admin

# Register your models here.
# Each model should be registered using: admin.site.register(<Model>)

from music.models import Performer, Festival

admin.site.register(Performer)
admin.site.register(Festival)
