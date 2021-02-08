from django.db import models
from django.db.models.deletion import SET_NULL, SET_DEFAULT
from django.utils.translation import gettext as _
from django.urls import reverse
from django.contrib.auth.models import User  
  
# Модель таблицы пользователей
class UserProfile(models.Model):  
    age = models.IntegerField()  
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

# Модель таблицы базы данных авторов книг
class Author(models.Model):
    full_name = models.TextField(verbose_name=_("Имя автора"))
    birth_year = models.SmallIntegerField(verbose_name=_("Год рожения"))
    country = models.CharField(max_length=2, verbose_name=_("Страна"))

    def __str__(self):
        return self.full_name
    def get_absolute_url(self):
        return reverse('home_library:authors')    

# Модель таблицы базы данных друзей
class Friend(models.Model):
    full_name = models.TextField(verbose_name=_("Имя друга"))
    address = models.TextField(verbose_name=_("Адрес"))
    phone = models.TextField(verbose_name=_("Телефон"))
    def __str__(self):
            return self.full_name
    def get_absolute_url(self):
        return reverse('home_library:friends')   

# Модель таблицы базы данных издательств
class Publisher(models.Model):
    name = models.TextField(verbose_name='Название')
    address = models.TextField(verbose_name='Юридический адрес')
    web = models.TextField(verbose_name='Web-сайт')
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('home_library:publishers')   

# Модель таблицы базы данных книг
class Book(models.Model):
    ISBN = models.CharField(max_length=13,
                            verbose_name=_("Международный стандартный "
                                           "книжный номер"))
    title = models.TextField(verbose_name=_("Название"))
    description = models.TextField(verbose_name=_("Аннотация"))
    year_release = models.SmallIntegerField(verbose_name=_("Год издания"))
    copy_count = models.SmallIntegerField(verbose_name=_("Число копий"), null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, null=True,
                                verbose_name=_("Цена"))
    author = models.ForeignKey("home_library.Author", on_delete=models.CASCADE,
                               verbose_name=_("Автор"), related_name="book_author")
    publisher = models.ForeignKey("home_library.publisher", on_delete=SET_NULL, null=True, 
                                  verbose_name=_("Издательство"), related_name="book_publisher")
    friends = models.ForeignKey("home_library.Friend", on_delete=SET_NULL, null=True, verbose_name=_("Должник"), related_name="book_friend")
    photo = models.ImageField(upload_to='book_photo', blank=True, verbose_name=_("Изображение книги"), null=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('home_library:index')   


