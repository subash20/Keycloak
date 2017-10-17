from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^secure$', views.secure, name='secure'),
    url(r'^lms',views.lms,name='lms'),
    #url(r'^qis',views.qis,name='qis'),
    url(r'^page',views.page,name='page'),
    url(r'^qispage',views.qispage,name='qispage'),
    url(r'^upload',views.upload,name='upload')
]