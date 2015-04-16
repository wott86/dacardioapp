from django.contrib import admin
from apps.patients import models
import pyclbr

# Register your models here.
classes = pyclbr.readmodule_ex(models.__name__)
for model in classes:
    admin.site.register(getattr(models, model))
