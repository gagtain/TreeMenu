from django.urls import path, include, re_path
from tree_menu.views import index
urlpatterns = [
    re_path(r'^(.*)/$', index, name='index'),
    path('', index, name='index'),
]