from django.conf.urls import url
from ..views import (RunwayListView, RunwayCreateView, RunwayDetailView,
                     RunwayUpdateView, RunwayDeleteView,runwayAssignment)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        RunwayCreateView.as_view(),
        name="runway_create"),

    url(r'^(?P<pk>\d+)/update/$',
        RunwayUpdateView.as_view(),
        name="runway_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        RunwayDeleteView.as_view(),
        name="runway_delete"),

    url(r'^(?P<pk>\d+)/$',
        RunwayDetailView.as_view(),
        name="runway_detail"),

    url(r'^assignment/$',
        runwayAssignment,
        name="runway_assignment"),

    url(r'^$',
        RunwayListView.as_view(),
        name="runway_list"),
]
