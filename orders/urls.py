from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^created/$', views.order_create, name='order_created'),
    re_path(r'^create/$', views.order_create, name='order_create'),

]