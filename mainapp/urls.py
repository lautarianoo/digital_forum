from django.urls import path
from .views import MainPage, TakePart, AboutUs, QuestionView

urlpatterns = [
    path('', MainPage.as_view(), name='main_page'),
    path('takepart', TakePart.as_view(), name='take_part'),
    path('about_us', AboutUs.as_view(), name='about_us'),
    path('questions', QuestionView.as_view(), name='questions')
]