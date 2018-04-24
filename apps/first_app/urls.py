from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),    # This line has changed! Notice that urlpatterns is a list, the comma is in
    url(r'^process$', views.process),    # This line has changed! Notice that urlpatterns is a list, the comma is in
    url(r'^results$', views.results),    # This line has changed! Notice that urlpatterns is a list, the comma is in
    url(r'^users/new$', views.addnew),    # This line has changed! Notice that urlpatterns is a list, the comma is in
    url(r'^add_newitem$', views.add_newitem),    # This line has changed! Notice that urlpatterns is a list, the comma is in
    url(r'^login$', views.login),    # This line has changed! Notice that urlpatterns is a list, the comma is in
    url(r'^logout$', views.logout),    # This line has changed! Notice that urlpatterns is a list, the comma is in
    url(r'^delete/(?P<item_id>\d+)$', views.delete),    # This line has changed! Notice that urlpatterns is a list, the comma is in
    url(r'^add_to_my_list/(?P<item_id>\d+)$', views.add_to_my_list),    # This line has changed! Notice that urlpatterns is a list, the comma is in
    url(r'^remove_item/(?P<item_id>\d+)$', views.remove_item),    # This line has changed! Notice that urlpatterns is a list, the comma is in
    url(r'^show_item/(?P<item_id>\d+)$', views.show_item),    # This line has changed! Notice that urlpatterns is a list, the comma is in
    
   # This line has changed! Notice that urlpatterns is a list, the comma is in
                                # url(r'^test', views.test),   # This line has changed! Notice that urlpatterns is a list, the comma is in
]                   
