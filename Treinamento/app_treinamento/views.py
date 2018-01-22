# -*- coding: utf-8 -*-
from __future__ import unicode_literals, division

from django.shortcuts import render
from .models import Aluno

# Create your views here.


def home_app(request, part_string):

    alunos = Aluno.objects.all()

    # select * from aluno where name like '%r'

    data = {
        "alunos": alunos
    }
    return render(request=request, template_name='index.html', context=data)