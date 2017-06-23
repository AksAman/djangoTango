from django.conf.urls import url
from . import views


urlpatterns= [
    #HomePage
    url(r'^$', views.index, name='colleges'),
    #college/112/
    url(r'^(?P<college_id>[0-9]+)/',views.details, name ='details'),
]
