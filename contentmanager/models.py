from django.db import models

# Create your models here.

class Elder(models.Model):
    first_name = models.CharField("Имя", max_length=50)
    second_name = models.CharField("Фамилия", max_length=50)
    bio = models.TextField("Короткая справка",)
    avatar = models.ImageField("Аватар", upload_to='elders/')
    email = models.CharField("Почта", blank=True, max_length=100)

    def __str__(self):
        return '%s %s' % (self.first_name, self.second_name)
