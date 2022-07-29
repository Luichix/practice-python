from django.urls import path

from webApp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('service/', views.service, name='service'),
    path('store/', views.store, name='store'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
]
