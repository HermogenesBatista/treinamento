# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Treinamento.settings2")

django.setup()

# daqui, importar os models

from app_treinamento import models

new_students = [
    {
        "name": "Hermogenes Filho",
        "age": 17
    },
    {
        "name": "Luana",
        "age": 18
    },
]

for data_student in new_students:
    student = models.Aluno(**data_student)
    student.save()
