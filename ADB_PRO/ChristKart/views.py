from django.shortcuts import render
from django.views.generic import (View,TemplateView)
# Create your views here.


class index(TemplateView):
    template_name = 'index.html';
class plates(TemplateView):
    template_name = 'plates.html'

class bags(TemplateView):
    template_name = 'bags.html'
class straws(TemplateView):
    template_name = 'straws.html'
