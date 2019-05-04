from django.urls import re_path
from shop import views

urlpatterns = [
    re_path(r'^$', views.IndexView.as_view(), name='index'),
    re_path(
        r'^category/(?P<publication_id>[\d]+)/$',
        views.CategoryView.as_view(),
        name='category'
    ),
    re_path(
        r'^item/(?P<publication_id>[\d]+)/$',
        views.ItemView.as_view(),
        name='item'
    )
]