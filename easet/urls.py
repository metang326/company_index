from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^home/$',views.home,name='home'),
    url(r'^aboutUS/$',views.aboutUS,name='aboutUS'),
    url(r'^business/$',views.business,name='business'),
    url(r'^products/$',views.products,name='products'),
    url(r'^job/$',views.job,name='job'),
    url(r'^contactUS/$',views.contactUS,name='contactUS'),
]