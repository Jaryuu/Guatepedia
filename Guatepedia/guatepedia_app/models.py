from django.db import models

from django.contrib.auth.models import User

class Investigador(models.Model):
    user = models.OneToOneField(User)
    ## En futuro...
    #investigacion = foreignKey(Investigacion)
from django.db import models

# Create your models here.
