__author__ = 'alvaro'
import inspect
from django.contrib import admin
import pyclbr
from django.db import models


def register_models(my_models, admins=None):
    """
    Call this from your admin.py in your app, this will register all your models

    Example:
        # my_app/admin.py
        from my_app import models
        from utils.admin import register_models

        register_models(models)

    :param my_models: your models module
    :param admins: your custom admins, must be a dictionary like {'MyModel': <MyModelAdmin>}
    """
    admins = {} if admins is None else admins
    classes = pyclbr.readmodule_ex(my_models.__name__)
    for model in classes:
        model = getattr(my_models, model)
        if inspect.isclass(model) and issubclass(model, models.Model):
            if model.__name__ in admins:
                admin.site.register(model, admins[model.__name__])
            else:
                admin.site.register(model)