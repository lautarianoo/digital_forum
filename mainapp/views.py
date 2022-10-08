from django.shortcuts import render
from django import views

class MainPage(views.View):

    def get(self, request, *args, **kwargs):
        return render(request, "mainapp/main_page.html", {})