from django.urls import path,re_path
from . import views

urlpatterns=[
	path('',views.base,name='base'),
	path('basic/create',views.create,name='create'),
	path('basic/read',views.read,name='read'),
	path('basic/<id_no>/detailsofuser', views.detailsofuser,name='detailsofuser'),
	path('basic/<id_no>/edituser',views.edituser,name='edituser'),
	path('basic/<id_no>/deleteuser',views.deleteuser,name='deleteuser'),
]