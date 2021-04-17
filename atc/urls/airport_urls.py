from django.conf.urls import url
from ..views import (AirportListView, AirportCreateView, AirportDetailView,
                     AirportUpdateView, AirportDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        AirportCreateView.as_view(),
        name="airport_create"),

    url(r'^(?P<pk>\d+)/update/$',
        AirportUpdateView.as_view(),
        name="airport_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        AirportDeleteView.as_view(),
        name="airport_delete"),

    url(r'^(?P<pk>\d+)/$',
        AirportDetailView.as_view(),
        name="airport_detail"),

    url(r'^$',
        AirportListView.as_view(),
        name="airport_list"),
]
