from django.conf.urls import patterns, url
from guatepidia import views

urlpatterns = patterns('',
	url('index', views.index, name='gpindex'))