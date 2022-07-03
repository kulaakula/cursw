from django.db import models

class HardSkills(models.Model):
    # respondent = models.IntegerField(verbose_name=, )
    # coworker = models.IntegerField(verbose_name=, )
    # criteria = models.IntegerField(verbose_name=, )
    completed = models.BooleanField(verbose_name='Выполнено?', default=False)

class HardSkillsCriterias(models.Model):
    title = models.CharField(verbose_name='', max_length=255)
    description = models.TextField(verbose_name='')
