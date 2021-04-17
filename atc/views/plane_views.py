from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Plane, Airport
from ..forms import PlaneForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from math import sqrt, degrees, atan2
from ..helpers import calc_heading, calc_distance, all_air_collisions, send_imminent_collision_post
import json
from braces.views import SuperuserRequiredMixin, StaffuserRequiredMixin
from dateutil import parser
import pytz


utc=pytz.UTC


@csrf_exempt
def handle_plane_payload(request):
    body = json.loads(request.body)
    
    plane = Plane.objects.filter(identifier=body["plane"]).first()
    direction = float(body["direction"])
    speed = float(body["speed"])
    origin = Airport.objects.filter(name=body["origin"]).first()
    destination = Airport.objects.filter(name=body["destination"]).first()
    take_off_time = utc.localize(parser.parse(body["take_off_time"]))
    landing_time = utc.localize(parser.parse(body["landing_time"]))

    plane.take_off_airport = origin
    plane.land_airport = destination
    plane.take_off_time = take_off_time
    plane.landing_time = landing_time
    plane.heading = direction
    plane.speed = speed
    plane.runway = None
    plane.save()

    all_air_collisions(plane)
    
    return HttpResponse()


class PlaneListView(ListView):
    model = Plane
    template_name = "atc/plane_list.html"
    paginate_by = 20
    context_object_name = "plane_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        super(PlaneListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PlaneListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PlaneListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(PlaneListView, self).get_queryset()

    def get_allow_empty(self):
        return super(PlaneListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(PlaneListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(PlaneListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(PlaneListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(PlaneListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(PlaneListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(PlaneListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PlaneListView, self).get_template_names()


class PlaneDetailView(DetailView):
    model = Plane
    template_name = "atc/plane_detail.html"
    context_object_name = "plane"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        super(PlaneDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PlaneDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PlaneDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(PlaneDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(PlaneDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(PlaneDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(PlaneDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(PlaneDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(PlaneDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PlaneDetailView, self).get_template_names()


class PlaneCreateView(SuperuserRequiredMixin, CreateView):
    model = Plane
    form_class = PlaneForm
    template_name = "atc/plane_create.html"
    success_url = reverse_lazy("plane_list")

    def __init__(self, **kwargs):
        super(PlaneCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(PlaneCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PlaneCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(PlaneCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(PlaneCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(PlaneCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(PlaneCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(PlaneCreateView, self).get_initial()

    def form_invalid(self, form):
        response = super(PlaneCreateView, self).form_invalid(form)
        response.status_code = 400
        return response

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(PlaneCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(PlaneCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(PlaneCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PlaneCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("atc:plane_detail", args=(self.object.pk,))


class PlaneUpdateView(StaffuserRequiredMixin, UpdateView):
    model = Plane
    form_class = PlaneForm
    template_name = "atc/plane_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "plane"

    def __init__(self, **kwargs):
        super(PlaneUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PlaneUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PlaneUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(PlaneUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(PlaneUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(PlaneUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(PlaneUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(PlaneUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        form = super(PlaneUpdateView, self).get_form(form_class)
        form.process_perms(self.request)
        return form

    def get_form_kwargs(self, **kwargs):
        return super(PlaneUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(PlaneUpdateView, self).get_initial()

    def form_invalid(self, form):
        response = super(PlaneUpdateView, self).form_invalid(form)
        response.status_code = 400
        return response

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(PlaneUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(PlaneUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_success_url(self):
        return reverse("atc:plane_detail", args=(self.object.pk,))


class PlaneDeleteView(SuperuserRequiredMixin, DeleteView):
    model = Plane
    template_name = "atc/plane_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "plane"

    def __init__(self, **kwargs):
        super(PlaneDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PlaneDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(PlaneDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(PlaneDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(PlaneDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(PlaneDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(PlaneDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(PlaneDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(PlaneDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(PlaneDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PlaneDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("atc:plane_list")
