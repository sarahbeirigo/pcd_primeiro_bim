from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Raffle)
admin.site.site_header = "Rifando Admin"