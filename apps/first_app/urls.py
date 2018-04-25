from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),    # This line has changed! Notice that urlpatterns is a list, the comma is in
    url(r'^process$', views.process),    # This line has changed! Notice that urlpatterns is a list, the comma is in
    url(r'^results$', views.results),    # This line has changed! Notice that urlpatterns is a list, the comma is in
    url(r'^add_newquote$', views.addquote),    # This line has changed! Notice that urlpatterns is a list, the comma is in
    url(r'^addtofavlist/(?P<quote_id>\d+)$', views.addtolist),    # This line has changed! Notice that urlpatterns is a list, the comma is in
    url(r'^removefromlist/(?P<quote_id>\d+)$', views.removefromlist),    # This line has changed! Notice that urlpatterns is a list, the comma is in
    url(r'^showuser/(?P<user_id>\d+)$', views.showuser),    # This line has changed! Notice that urlpatterns is a list, the comma is in
    url(r'^login$', views.login),    # This line has changed! Notice that urlpatterns is a list, the comma is in
    url(r'^logout$', views.logout),    # This line has changed! Notice that urlpatterns is a list, the comma is in
    
   # This line has changed! Notice that urlpatterns is a list, the comma is in
                                # url(r'^test', views.test),   # This line has changed! Notice that urlpatterns is a list, the comma is in
]                   
