from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
import guatepediaapp.views as views
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Guatepedia.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^buscar/',views.buscar,name="buscar"),

)


