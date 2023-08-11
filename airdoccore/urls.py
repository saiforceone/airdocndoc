
# Generated using D.I.R.T Stack CLI

from django.urls import path

from . import views


urlpatterns = [
	path('', views.index, name='airdoccore')
]


