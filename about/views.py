from django.shortcuts import render
from django.views.generic.base import TemplateView


class AboutMeView(TemplateView):
    template_name = 'about/me.html'
