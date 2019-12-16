
from loginApp import views

from django.conf.urls import url
from django.urls import path

urlpatterns = [

	#url(r'^$',views.index,name='index'),
	path('',views.index,name='index'),
	#path('logout/',views.index,name='index'),

	path('logout/',views.logout,name='logout'),
	path('profile/',views.profile,name='profile')
]
