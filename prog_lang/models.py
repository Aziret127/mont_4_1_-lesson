from django.db import models

# Create your models here.


class ProgLang(models.Model):
    #Charfield - поле которое отвечает за кол-во символов в форме
    #max_length - максимальное кол-во символов
    title = models.CharField(max_length=100, verbose_name="укажите язык программирования")
    #TextField - указывает не ограниченая кол-во символов
    description = models.TextField(verbose_name="описание языка программирования")
    #ImageField - поле для загрузки изображений - принимает любой формат
    image = models.ImageField(upload_to="proglang/", verbose_name="изображение языка программирования")
    #PositiveIntegerField - указывает на то что нужно загружать только положительные числа, blank=True - поле не обязательное для заполнения
    crated_date_lang = models.PositiveIntegerField(verbose_name="год создания языка программирования", blank=True)

    file_python = models.FileField(upload_to='files/', verbose_name='загрузите какой нибудь файл', null=True)

    viki_url = models.URLField(verbose_name='вставьте ссылку с википедии', null=True)

    views = models.PositiveIntegerField(default=0, null=True)

    #DateTimeField - поле для хранения даты и времени auto_now_add - при создании записи автоматически сохраняет дату и время создания
    created_at = models.DateTimeField(auto_now_add=True,)

#TODO - изуучить поля самостоятельно FileField, URLField, EmailField, и ище доп кокие нибудь поля
#!!!! атребут null=True - позволяет сохранять пустые значения в базе данных

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "язык программирования"
        verbose_name_plural = "языки программирования"