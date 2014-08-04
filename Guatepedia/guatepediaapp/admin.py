from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from models import *
from categories.admin import CategoryBaseAdmin
from categories.models import *
from mce_filebrowser.admin import MCEFilebrowserAdmin

class InvestigadorInline(admin.StackedInline):
    ##Para agregar mas campos al admin panel
    model = Investigador
    can_delete = False
    verbose_name_plural = 'Investigadores'

# Configurar campos del formulario del UserAdmin
class UserAdmin(UserAdmin):
    inlines = (InvestigadorInline, ) ##Agregando los inlines al formulario
    def get_form(self, request, obj=None, **kwargs):
        ## Excluyendo la forma de permisos para que unicamente se manejen los grupo como permisos
        self.exclude = ("user_permissions")
        ## Agregando campos de usuario acvitvo, staff o superousuario y grupos de permisos.
        self.fieldsets[2][1]["fields"] = ('is_active', 'is_staff','is_superuser','groups')
        form = super(UserAdmin,self).get_form(request, obj, **kwargs)
        return form

class InvestigacionAdmin(MCEFilebrowserAdmin):
    #Atributos para mostrar informacion en forma de tabla en el admin de Django
    list_display = ('titulo','get_autores','estado','fecha')
    list_display_links = ('titulo','get_autores','estado','fecha')
    list_per_page = 20
    ordering = ['titulo']
    search_fields = ['titulo','get_autores','estado']

    def save_model(self, request, obj, form, change):
        original = Investigacion()
        if change:
            original = Investigacion.objects.get(pk=obj.pk)
        #Verificamos si el contenido ha cambiado
        if original.contenido != obj.contenido:
            obj.estado = 3
        obj.user = request.user
        obj.save()

    def get_readonly_fields(self, request, obj=None):
        if self.is_investigador(request): # editing an existing object
            return self.readonly_fields + ('estado',)
        return self.readonly_fields

    def is_verificador(self,request):
        return request.user.groups.filter(name='VerificadorContenido')
    def is_investigador(self,request):
        return request.user.groups.filter(name='Investigadores')

    #Metodo filtra las investigaciones para mostrar unicamente las que son del autor
    def queryset(self,request):
        qs = Investigacion.objects.all()
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(autor=request.user)
    #Metodo para seleccionar autmaticamente el autor de la investgacion que se crea

    #def formfield_for_manytomany(self, db_field, request=None, **kwargs):
    #    if db_field.name == 'autor':
    #        kwargs['initial'] = request.user.id
    #    return super(InvestigacionAdmin, self).formfield_for_manytomany( db_field, request, **kwargs)



class InvestigacionPendienteAdmin(admin.ModelAdmin):
    pass
    def queryset(self,request):
        return self.model.objects.filter(estado=5)

class SimpleCategoryAdmin(CategoryBaseAdmin):
    pass


admin.site.register(Categoria,SimpleCategoryAdmin)
admin.site.register(InvestigacionPendiente,InvestigacionPendienteAdmin)
admin.site.register(Investigacion,InvestigacionAdmin)
# Re-registrando UserAdmin en el panel de administracion
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Category)