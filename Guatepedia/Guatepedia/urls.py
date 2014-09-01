from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
import guatepediaapp.views as views
from django.conf.urls.static import static
from guatepediaapp import urls as gurls

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Guatepedia.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/guatepediaapp/investigacion/(?P<id>[0-9]+)/solicitar_aprobacion/',views.solicitar_aprobacion,name="solicitar_aprobacion"),
    url(r'^admin/guatepediaapp/investigacion/(?P<id>[0-9]+)/publicar_investigacion/',views.publicar_investigacion,name="publicar_investigacion"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^guatepedia/', include(gurls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^mce_filebrowser/', include('mce_filebrowser.urls')),
    url(r'^taggit_autocomplete/', include('taggit_autocomplete.urls')),
    url(r"^search/", include("watson.urls", namespace="watson"))
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


