from django.db import models

from django.contrib.auth.models import User

User._meta.get_field_by_name('email')[0]._unique = True

class Investigador(models.Model):
    ##Esto incluye nombre,apellido,correo,password,fecha de creacion,y permisos de grupo
    user = models.OneToOneField(User)

    ## En futuro...(Next Scrum)
    #investigacion = foreignKey(Investigacion)
