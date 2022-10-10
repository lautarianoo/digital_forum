from django.contrib import messages
from django.shortcuts import render, redirect
from django import views
from .models import ParticipantEvent, QuestionAnswer

class MainPage(views.View):

    def get(self, request, *args, **kwargs):
        return render(request, "mainapp/main_page.html", {})

class TakePart(views.View):

    def get(self, request, *args, **kwargs):
        return render(request, "mainapp/take_part.html", {})

    def post(self, request, *args, **kwargs):
        if not ParticipantEvent.objects.filter(email=request.POST.get('email')) or not ParticipantEvent.objects.filter(number_phone=request.POST.get('telephone')):
            new_participant = ParticipantEvent.objects.create(first_name=request.POST.get('name_user'), last_name=request.POST.get('surname_user'),
                                                              email=request.POST.get('email'), number_phone=request.POST.get('telephone'))
            new_participant.save()
            messages.add_message(request, messages.SUCCESS, 'Заявка успешно отправлена, на почту будут высланы подробности')
            return redirect("take_part")
        messages.add_message(request, messages.SUCCESS, 'Вы уже подавали заявку')
        return redirect("take_part")

class AboutUs(views.View):

    def get(self, request, *args, **kwargs):
        return render(request, "mainapp/about_us.html", {})

class QuestionView(views.View):

    def get(self, request, *args, **kwargs):
        questions = QuestionAnswer.objects.all()
        return render(request, "mainapp/questions.html", {"questions": questions})