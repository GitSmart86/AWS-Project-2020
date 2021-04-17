from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Runway, Plane, Airport
from ..forms import RunwayForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse
#<<<<<<< add-assignment-urls
from ..helpers import find_duplicate_runway

from braces.views import SuperuserRequiredMixin
from dateutil import parser
import pytz
utc=pytz.UTC
#=======
#<<<<<<< HEAD
from ..helpers import find_duplicate_runway
#=======
from braces.views import SuperuserRequiredMixin

#>>>>>>> 6d06b45430a31e64511f653aeaadc80c79cfc74c
#>>>>>>> master

@csrf_exempt
def runwayAssignment(request):
    body = json.loads(request.body)

    plane = Plane.objects.filter(identifier=body["plane"]).first()
    runway = Runway.objects.filter(identifier=body["runway"]).first()
    
    plane.runway = runway
    if "arrive_at_time" in body:
        date = utc.localize(parser.parse(body["arrive_at_time"]))
        plane.arrive_at_runway_time = date
        plane.save()
    else: # if there is no arriave at time, then we are at the game
        plane.arrive_at_runway_time = None
        plane.gate = None
        plane.heading = 0
        plane.speed = 0
        plane.take_off_airport = plane.land_airport
        plane.land_airport = None
        plane.take_off_time = None
        plane.landing_time = None
    
    plane.save()
    
    find_duplicate_runway(plane)
    
    return HttpResponse()


class RunwayListView(ListView):
    model = Runway
    template_name = "atc/runway_list.html"
    paginate_by = 20
    context_object_name = "runway_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        super(RunwayListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(RunwayListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(RunwayListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(RunwayListView, self).get_queryset()

    def get_allow_empty(self):
        return super(RunwayListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(RunwayListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(RunwayListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(RunwayListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(RunwayListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(RunwayListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(RunwayListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RunwayListView, self).get_template_names()


class RunwayDetailView(DetailView):
    model = Runway
    template_name = "atc/runway_detail.html"
    context_object_name = "runway"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        super(RunwayDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(RunwayDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(RunwayDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(RunwayDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(RunwayDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(RunwayDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(RunwayDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(RunwayDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(RunwayDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RunwayDetailView, self).get_template_names()


class RunwayCreateView(SuperuserRequiredMixin, CreateView):
    model = Runway
    form_class = RunwayForm
    template_name = "atc/runway_create.html"
    success_url = reverse_lazy("runway_list")

    def __init__(self, **kwargs):
        super(RunwayCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(RunwayCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(RunwayCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(RunwayCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(RunwayCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(RunwayCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(RunwayCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(RunwayCreateView, self).get_initial()

    def form_invalid(self, form):
        response = super(RunwayCreateView, self).form_invalid(form)
        response.status_code = 400
        return response

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(RunwayCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(RunwayCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(RunwayCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RunwayCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("atc:runway_detail", args=(self.object.pk,))


class RunwayUpdateView(SuperuserRequiredMixin, UpdateView):
    model = Runway
    form_class = RunwayForm
    template_name = "atc/runway_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "runway"

    def __init__(self, **kwargs):
        super(RunwayUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(RunwayUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(RunwayUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(RunwayUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(RunwayUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(RunwayUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(RunwayUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(RunwayUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(RunwayUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(RunwayUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(RunwayUpdateView, self).get_initial()

    def form_invalid(self, form):
        response = super(RunwayUpdateView, self).form_invalid(form)
        response.status_code = 400
        return response

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(RunwayUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(RunwayUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(RunwayUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(RunwayUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RunwayUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("atc:runway_detail", args=(self.object.pk,))


class RunwayDeleteView(SuperuserRequiredMixin, DeleteView):
    model = Runway
    template_name = "atc/runway_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "runway"

    def __init__(self, **kwargs):
        super(RunwayDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(RunwayDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(RunwayDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(RunwayDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(RunwayDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(RunwayDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(RunwayDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(RunwayDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(RunwayDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(RunwayDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RunwayDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("atc:runway_list")
