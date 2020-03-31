# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def first(request):
    return HttpResponse('Onlayn kutubxonaga xush kelibsiz')