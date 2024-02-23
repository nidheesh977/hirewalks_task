from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name_plural = "Users"
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Address(models.Model):
    class Meta:
        verbose_name_plural = "Addresses"
    title = models.CharField(max_length = 200)
    buyer = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    fullName = models.CharField(max_length = 100, null = True)
    addressLine1 = models.CharField(max_length = 200, null = True)
    addressLine2 = models.CharField(max_length = 200, null = True, blank = True)
    city = models.CharField(max_length = 200, null = True)
    state = models.CharField(max_length = 200, null = True)
    pincode = models.CharField(null = True, max_length = 20)
    country = models.CharField(null = True, max_length = 100)
    mobile = models.CharField(null = True, max_length = 15)

    def __str__(self):
        return self.title