from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, login, password=None):
        user = self.model(login=login)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, login, password):
        user = self.create_user(login=login, password=password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin): 
    login = models.CharField(unique=True, max_length=255, verbose_name="Логин") 
    first_name = models.CharField(max_length=255, verbose_name="Имя")
    last_name = models.CharField(max_length=255, verbose_name="Фамилия")
    middle_name = models.CharField(max_length=255, verbose_name="Отчество", blank=True)
    date_of_birth = models.DateField(verbose_name="Дата рождения", blank=True, null=True)
    photo = models.ImageField(verbose_name="Фото", upload_to="user", blank=True)

    is_active = models.BooleanField(verbose_name="Активация аккаунта", default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "login"
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.login
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    


