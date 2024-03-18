from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from .enums import User_Type


class AllUser(BaseUserManager):
    def create_user(self, phone, email, username, full_name, password=None, **kwargs):
        
        if not email:
            raise ValueError('need Email')
        
        if not username:
            raise ValueError('need Username')
        
        if not phone:
            raise ValueError('need Phone number')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            phone=phone,
            full_name=full_name,
            **kwargs,
        )
        user.is_active = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staff(self, phone, email, username, full_name, password):
        user = self.create_user(
            email=email,
            username=username,
            phone=phone,
            full_name=full_name,
            password=password,
        )
        user.is_staff = True
        user.is_active  = False
        user.is_superuser = False        
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, email, username, full_name, password):
        user = self.create_user(
            email=email,
            username=username,
            phone=phone,
            full_name=full_name,
            password=password,
        )
        user.is_staff     = True
        user.is_active    = True
        user.is_superuser = True  
        user.is_admin     = True      
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', message='only alphabets and ascci characters')
    numbers      = RegexValidator(r'^[0-9a]*$', message='only numbers')
    phone        = models.CharField(max_length=11, unique=True)
    email        = models.EmailField(unique=True)
    username     = models.CharField(max_length=30, unique=True)
    full_name    = models.CharField(max_length=100)
    is_active    = models.BooleanField(default=True)
    is_staff     = models.BooleanField(default=False)    
    is_admin     = models.BooleanField(default=False)
    last_login   = models.DateTimeField(null=True, blank=True)
    created_at   = models.DateTimeField(auto_now_add=True)
    role         = models.PositiveSmallIntegerField(choices=User_Type.ROLE, default=2)
    
    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["email", "username", "full_name"]
    
    objects = AllUser()

    def __str__(self) -> str:
        return self.phone
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


class UserOTP(models.Model):
    numbers    = RegexValidator(r'^[0-9a]*$', message='only numbers')
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    otp        = models.CharField(max_length=6, validators=[numbers], unique=True)
    otp_type   = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'    


class Profile(models.Model):
    user      = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    phone     = models.CharField(max_length=11, unique=True)
    email     = models.EmailField(unique=True)
    username  = models.CharField(max_length=30, unique=True)
    full_name = models.CharField(max_length=100)
    pic       = models.ImageField(upload_to='profile/', blank=True, null=True)
    address   = models.CharField(max_length=550, blank=True, null=True)
    city      = models.CharField(max_length=20, blank=True, null=True)
    post_id   = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.user} {self.phone}'
