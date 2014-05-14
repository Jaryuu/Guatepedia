from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from guatepedia_app.models import Investigador

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class InvestigadorInline(admin.StackedInline):
    ##Para agregar mas campos al admin panel
    model = Investigador
    can_delete = False
    verbose_name_plural = 'Investigador'

# Define a new User admin
class UserAdmin(UserAdmin):
    ##Descomentar para agregar nuevos campos al modelAdmin del Usuario
   # inlines = (InvestigadorInline, ) ##Agregando los inlines al form

    def get_form(self, request, obj=None, **kwargs):
        ## Excluyendo la forma de permisos para que unicamente se manejen los grupo como permisos
        self.exclude = ("user_permissions")
        ## Dynamically overriding
        self.fieldsets[2][1]["fields"] = ('is_active', 'is_staff','is_superuser','groups')
        form = super(UserAdmin,self).get_form(request, obj, **kwargs)
        return form

# Re-registrando UserAdmin en el panel de administracion
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
#
