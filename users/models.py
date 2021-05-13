from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import Group

#Crear un nuevo usuario
#Crear un superusuario


class MyAccountManager(BaseUserManager):

    def create_user(self, email, dni, first_name, last_name, password=None):
        '''Crea una Account con el email'''
        values = [email, dni, first_name, last_name ]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
        for field_name, value in field_value_map.items():
            if not value:
                raise ValueError('El valor {} debe estar seteado'.format(field_name))

        user = self.model(
            email = self.normalize_email(email),
            dni = dni,
            first_name = first_name,
            last_name = last_name,
            
            )
        user.set_password(password)
        user.save(using=self._db)
        return user
    

    # def create_bus_driver(self, email, dni, first_name, last_name, tipo_de_usuario, password):
    #     user = self.create_user(
    #         email = self.normalize_email(email),
    #         dni = dni,
    #         first_name = first_name,
    #         last_name = last_name,
    #         password=password,
    #         tipo_de_usuario=tipo_de_usuario,
    #     )
    #     user.tipo_de_usuario = 1 #Es chofer
    #     user.is_staff = True #El chofer es staff
    #     user.tipo_de_usuario
    #     user.save(using=self._db)
    #     return user


    def create_superuser(self, email, dni, first_name, last_name, password):
        user = self.create_user(
            email = self.normalize_email(email),
            dni = dni,
            first_name = first_name,
            last_name = last_name,
            password=password
        )
        user._is_admin =  True
        user.is_staff = True
        user._is_superuser = True

        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email               = models.EmailField(verbose_name="email", max_length=60, unique=True)
    dni                 = models.IntegerField(verbose_name="dni", unique=True)
    first_name          = models.CharField(max_length=30)
    last_name           = models.CharField(max_length=30)
    date_of_birth       = models.DateField(blank=True, null=True)
    is_GOLD             = models.BooleanField(default=False)
    _is_admin           = models.BooleanField(default=False)
    is_active           = models.BooleanField(default=True)
    is_staff            = models.BooleanField(default=False)
    _is_superuser       = models.BooleanField(default=False)
    tipo_de_usuario     = models.BooleanField(default=0)
    
    objects = MyAccountManager()

    class Meta:
        verbose_name        = "Usuario"
        verbose_name_plural = "Usuarios"

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['dni', 'first_name', 'last_name']

    def tipo(self):
        return 0

    def __str__(self):
        return self.get_full_name()
        
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_name(self):
        return self.first_name
    
    def get_email(self):
        return self.email

    def has_perm(self, perm, obj=None):
        '''Función default para saber si el usuario tiene permisos para hacer cierta acción'''
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_admin(self):
        return self.is_staff

class Chofer(Account):

    class Meta:
        proxy = True
        permissions = (
            ("es_chofer", "Es un chofer"),
        )
        verbose_name_plural = "Choferes"

    def tipo(self):
        return 1
    
