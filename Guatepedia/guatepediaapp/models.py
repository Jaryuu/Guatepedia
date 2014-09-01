from django.db import models
from tinymce import models as tinymce_models
from django.contrib.auth.models import User
from django.contrib import admin
from categories.models import CategoryBase
from taggit_autocomplete.managers import TaggableManager
import django_tables2 as tables
import watson

class Investigacion(models.Model):
    autor = models.ManyToManyField(User)
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='fotos_investigacion/',verbose_name="Imagen Principal",help_text="Ingrese una imagen como vista previa de la investigacion")
    contenido = tinymce_models.HTMLField()
    referencias = models.TextField(verbose_name="Referencias Bibliograficas")
    dict_estados =((1,"Publicado"),(2,"Necesita Editarse"),(3,"Necesita Aprobacion"),(4,"Aprobado"),(5,"En Proceso de Aprobacion"))
    estado = models.IntegerField(choices=dict_estados,default=2)
    categoria = models.ManyToManyField('Categoria',blank=True)
    fecha = models.DateField(verbose_name="Fecha de Publicacion")
    tags = TaggableManager(verbose_name="Palabras clave", help_text="Ingrese las palabras clave separadas por un espacio",blank=True)

    @property
    def is_saved(self):
        try:
            Investigacion.objects.get(pk=self.pk)
            return True
        except obj.DoesNotExist:
            return False
    def get_autores(self):
        return "\n".join([a.username for a in self.autor.all()])
    get_autores.short_description = "Autores"
    def __unicode__(self):
        return self.titulo

    class Meta(object):
        verbose_name = 'Investigacion'
        verbose_name_plural = 'Investigaciones'

class InvestigacionPendiente(Investigacion):

    class Meta:
        verbose_name = 'Investigacion Pendiente'
        verbose_name_plural = 'Investigaciones Pendientes'
        proxy=True

class Categoria(CategoryBase):

    imagen = models.ImageField()
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural="Categorias"


#Clase para manejar los campos visibles en el panel de admin
ESTADO_VISIBLE = [1]
class ManejadorInvestigacion(models.Manager):

    def get_query_set(self):
        default_queryset = super(ManejadorInvestigacion,self).get_query_set()
        #Solo mostramos posts cuyo estado sea el visible
        return default_queryset.filter(status__in=ESTADO_VISIBLE)


class Investigador(models.Model):
    user = models.OneToOneField(User)

class TablaResultados(tables.Table):
    upload_to='fotos_categorias/',verbose_name="Imagen Principal",help_text="Ingrese una imagen como vista previa de la Categoria"
    class Meta:
        model = Person
        attrs = {'class':'paleblue'}

#Registrando Modelos en Buscador Watson
watson.register(Investigacion, fields=("titulo", "autor","categoria","contenido","tags"))