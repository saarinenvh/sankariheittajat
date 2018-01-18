from django.contrib import admin
from . import models

class uutisetAdmin(admin.ModelAdmin):
    list_display = ['aihe', 'aika', 'kirjoittaja']

admin.site.register(models.uutiset, uutisetAdmin)

# Register your models here.
