from django.conf.urls import url
from ..views import (GateListView, GateCreateView, GateDetailView,
                     GateUpdateView, GateDeleteView, gateAssignment)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        GateCreateView.as_view(),
        name="gate_create"),

    url(r'^(?P<pk>\d+)/update/$',
        GateUpdateView.as_view(),
        name="gate_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        GateDeleteView.as_view(),
        name="gate_delete"),

    url(r'^(?P<pk>\d+)/$',
        GateDetailView.as_view(),
        name="gate_detail"),

    url(r'^assignment/$',
        gateAssignment,
        name="gate_assignment"),

    url(r'^$',
        GateListView.as_view(),
        name="gate_list"),
]
