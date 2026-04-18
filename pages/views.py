from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class HomePageView(TemplateView):
    template_name = "home.html"


class WhatsNewPageView(TemplateView):
    template_name = "whatsnew.html"


class AboutPageView(TemplateView):
    template_name = "about.html"


class ContactPageView(TemplateView):
    template_name = "contact.html"
