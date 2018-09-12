from django.contrib import admin

from tasks import models

CRUD = [models.Student,
        models.Task,
        models.Answer,
        models.Group,
        models.Topic
        ]
admin.site.register(CRUD)
