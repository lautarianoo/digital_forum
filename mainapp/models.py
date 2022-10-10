from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class ParticipantEvent(models.Model):

    first_name = models.CharField("Имя", max_length=40)
    last_name = models.CharField("Фамилия", max_length=40)
    number_phone = models.CharField("Контактный номер телефона", max_length=12)
    email = models.EmailField("Почта", max_length=40)

    def __str__(self):
        return f"Участник №{self.id}"

    class Meta:
        verbose_name = "Участник мероприятия"
        verbose_name_plural = "Участники мероприятий"

class QuestionAnswer(models.Model):

    title_question = models.CharField("Вопрос", max_length=100)
    answer = models.TextField(verbose_name="Ответ")

    def __str__(self):
        return self.title_question

    class Meta:
        verbose_name="Часто задаваемый вопрос"
        verbose_name_plural="Часто задаваемые вопросы"

