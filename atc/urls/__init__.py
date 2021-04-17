from django.conf.urls import include, url

app_name="atc"

urlpatterns = [

    url(r'^airlines/', include('atc.urls.airline_urls')),  # NOQA
    url(r'^airports/', include('atc.urls.airport_urls')),
    url(r'^gates/', include('atc.urls.gate_urls')),
    url(r'^runways/', include('atc.urls.runway_urls')),
    url(r'^planes/', include('atc.urls.plane_urls')),
    url('', include('atc.urls.plane_urls')), # default atc page
]
