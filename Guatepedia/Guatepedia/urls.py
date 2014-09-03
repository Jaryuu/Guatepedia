from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
import guatepediaapp.views as views
import guatepidia.views as gpviews
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Guatepedia.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^index/',views.index, name="index"),
    url(r'^home/', views.home, name="home"),
    url(r'^home/investigacion/(?P<id>[0-9]+)/',views.mostrarInvestigacion, name="investigacion"),
    url(r'^admin/guatepediaapp/investigacion/(?P<id>[0-9]+)/solicitar_aprobacion/',views.solicitar_aprobacion,name="solicitar_aprobacion"),
    url(r'^admin/guatepediaapp/investigacion/(?P<id>[0-9]+)/publicar_investigacion/',views.publicar_investigacion,name="publicar_investigacion"),
    url(r'^guatepidia/', include('guatepidia.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^mce_filebrowser/', include('mce_filebrowser.urls')),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


