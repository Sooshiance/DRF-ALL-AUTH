from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from datetime import datetime


class AllUser(BaseUserManager):
    def create_user(self, phone, email, password=None, first_name=None, last_name=None):
        if not email:
            raise ValueError('کاربر باید پست الکترونیکی داشته باشد')
        
        if not phone:
            raise ValueError('کاربر باید شماره تلفن داشته باشد')
        
        if not first_name:
            raise ValueError('کاربر باید نام داشته باشد')
        
        if not last_name:
            raise ValueError('کاربر باید نام خانوادگی داشته باشد')

        user = self.model(
            email=self.normalize_email(email),
            phone=phone,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_active = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staff(self, phone, email, password, first_name, last_name):
        user = self.create_user(
            email=email,
            phone=phone,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_staff = True
        user.is_active  = False
        user.is_superuser = False        
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, email, password, first_name, last_name):
        user = self.create_user(
            email=email,
            phone=phone,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_staff = True
        user.is_active  = True
        user.is_superuser = True        
        user.save(using=self._db)
        return user


class Role:
    GOLDEN = 1
    SILVER = 2
    BRONZE = 3

    ROLES = (
        (GOLDEN, 'GOLDEN'),
        (SILVER, 'SILVER'),
        (BRONZE, 'BRONZE'),
    )


class User(AbstractBaseUser, PermissionsMixin):
    phone      = models.CharField(max_length=30, unique=True)
    email      = models.EmailField(unique=True)
    password   = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255)
    last_name  = models.CharField(max_length=255)
    image      = models.FileField(upload_to="users/", blank=True, null=True)
    is_locked  = models.BooleanField(default=False)
    is_staff   = models.BooleanField(default=False)
    
    # If it is set to False, users can't login to their accounts with their credentials until verified it
    is_active  = models.BooleanField(default=True)
    
    
    is_admin   = models.BooleanField(default=False)
    role       = models.PositiveSmallIntegerField(choices=Role.ROLES, default=3)
    last_login = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # If it is set to False, users need to verified their accounts with OTP
    verified   = models.BooleanField(default=True)
    
    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["email", "first_name", "last_name"]
    
    objects = AllUser()

    class Meta:
        ordering = ("-created_at",)
    
    @property
    def fullName(self):
        return str(self.first_name) + ' ' + str(self.last_name)

    def __str__(self) -> str:
        return self.phone

    def save_last_login(self) -> None:
        self.last_login = datetime.now()
        self.save()
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


class Profile(models.Model):
    user       = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='کاربر')
    email      = models.EmailField(verbose_name='پست الکترونیکی')
    phone      = models.CharField(max_length=11, verbose_name='شماره تماس')
    first_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='نام')
    last_name  = models.CharField(max_length=50, null=True, blank=True, verbose_name='نام خانوادگی')
    avatar     = models.FileField(upload_to="users/profile/", blank=True, null=True)
    role       = models.PositiveSmallIntegerField()
    
    @property
    def fullName(self):
        return str(self.first_name) + ' ' + str(self.last_name)
    
    def __str__(self) -> str:
        return f"{self.user} {self.email} {self.fullName} {self.role}"
