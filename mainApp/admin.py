from django.contrib import admin
from .models import Setting, Summary, Deal

# Register your models here.

admin.site.register(Setting)
admin.site.register(Summary)
admin.site.register(Deal)