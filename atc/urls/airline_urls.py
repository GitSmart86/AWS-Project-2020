from django.conf.urls import url
from ..views import (AirlineListView, AirlineCreateView, AirlineDetailView,
                     AirlineUpdateView, AirlineDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        AirlineCreateView.as_view(),
        name="airline_create"),

    url(r'^(?P<pk>\d+)/update/$',
        AirlineUpdateView.as_view(),
        name="airline_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        AirlineDeleteView.as_view(),
        name="airline_delete"),

    url(r'^(?P<pk>\d+)/$',
        AirlineDetailView.as_view(),
        name="airline_detail"),

    url(r'^$',
        AirlineListView.as_view(),
        name="airline_list"),
]
