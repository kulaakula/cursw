from turtle import title
from django.db import models


class SoftSkills(models.Model):
    # respondent = models.IntegerField(verbose_name=, )
    # coworker = models.IntegerField(verbose_name=, )
    # criteria = models.IntegerField(verbose_name=, )
    completed = models.BooleanField(verbose_name='Выполнено?', default=False)

class SoftSkillsCriterias(models.Model):
    title = models.CharField(verbose_name='', max_length=255)
    description = models.TextField(verbose_name='')


    def __str__(self) -> str:
        return self.login
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
