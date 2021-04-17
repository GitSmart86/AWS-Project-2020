from django.conf.urls import url
from ..views import (PlaneListView, PlaneCreateView, PlaneDetailView,
                     PlaneUpdateView, PlaneDeleteView, handle_plane_payload)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        PlaneCreateView.as_view(),
        name="plane_create"),

    url(r'^(?P<pk>\d+)/update/$',
        PlaneUpdateView.as_view(),
        name="plane_update"),

    url(r'^update/$',
        handle_plane_payload,
        name="plane_update_json"),

    url(r'^(?P<pk>\d+)/delete/$',
        PlaneDeleteView.as_view(),
        name="plane_delete"),

    url(r'^(?P<pk>\d+)/$',
        PlaneDetailView.as_view(),
        name="plane_detail"),

    url(r'^$',
        PlaneListView.as_view(),
        name="plane_list"),
]
