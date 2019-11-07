from django.urls import *
from . import views,testdb

urlpatterns =[
	re_path(r'^index/$', views.index, name='index'),
	path('', views.index,name='index'),
	path('hello',views.hello),

	re_path(r'^testdb$',testdb.saveName)
]
