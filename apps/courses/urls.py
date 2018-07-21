from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^course_add$', views.course_add),
    url(r'^course/remove/(?P<id>\d+)$', views.remove),
    url(r'^course/delete/(?P<id>\d+)$', views.destroy),
  ]