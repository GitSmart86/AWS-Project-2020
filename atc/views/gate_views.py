#<<<<<<< add-assignment-urls
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Gate, Plane, Airport
from ..forms import GateForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse
from ..helpers import find_duplicate_gate
from braces.views import SuperuserRequiredMixin
from dateutil import parser
import pytz


utc=pytz.UTC


@csrf_exempt
def gateAssignment(request):
    body = json.loads(request.body)

    print(body)
    plane = Plane.objects.filter(identifier=body["plane"]).first()
    gate = Gate.objects.filter(identifier=body["gate"]).first()
    
    if "arrive_at_time" in body:
        date = utc.localize(parser.parse(body["arrive_at_time"]))
        plane.arrive_at_gate_time = date
    else: # if there is no arriave at time, then we are at the game
        plane.arrive_at_gate_time = None
        plane.runway = None # if we are at the gate then we are not at the runway
    plane.save()
    
    find_duplicate_gate(plane)
    
    return HttpResponse()


class GateListView(ListView):
    model = Gate
    template_name = "atc/gate_list.html"
    paginate_by = 20
    context_object_name = "gate_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        super(GateListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(GateListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(GateListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(GateListView, self).get_queryset()

    def get_allow_empty(self):
        return super(GateListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(GateListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(GateListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(GateListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(GateListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(GateListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(GateListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(GateListView, self).get_template_names()


class GateDetailView(DetailView):
    model = Gate
    template_name = "atc/gate_detail.html"
    context_object_name = "gate"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        super(GateDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(GateDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(GateDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(GateDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(GateDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(GateDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(GateDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(GateDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(GateDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(GateDetailView, self).get_template_names()


class GateCreateView(SuperuserRequiredMixin, CreateView):
    model = Gate
    form_class = GateForm
    template_name = "atc/gate_create.html"
    success_url = reverse_lazy("gate_list")

    def __init__(self, **kwargs):
        super(GateCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(GateCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(GateCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(GateCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(GateCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(GateCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(GateCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(GateCreateView, self).get_initial()

    def form_invalid(self, form):
        response = super(GateCreateView, self).form_invalid(form)
        response.status_code = 400
        return response

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(GateCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(GateCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(GateCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(GateCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("atc:gate_detail", args=(self.object.pk,))


class GateUpdateView(SuperuserRequiredMixin, UpdateView):
    model = Gate
    form_class = GateForm
    template_name = "atc/gate_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "gate"

    def __init__(self, **kwargs):
        super(GateUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(GateUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(GateUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(GateUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(GateUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(GateUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(GateUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(GateUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(GateUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(GateUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(GateUpdateView, self).get_initial()

    def form_invalid(self, form):
        response = super(GateUpdateView, self).form_invalid(form)
        response.status_code = 400
        return response

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(GateUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(GateUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(GateUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(GateUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(GateUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("atc:gate_detail", args=(self.object.pk,))


class GateDeleteView(SuperuserRequiredMixin, DeleteView):
    model = Gate
    template_name = "atc/gate_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "gate"

    def __init__(self, **kwargs):
        super(GateDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(GateDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(GateDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(GateDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(GateDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(GateDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(GateDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(GateDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(GateDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(GateDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(GateDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("atc:gate_list")
#=======
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Gate, Plane, Airport
from ..forms import GateForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse
#<<<<<<< HEAD
from ..helpers import find_duplicate_gate
#=======
from braces.views import SuperuserRequiredMixin

#>>>>>>> 6d06b45430a31e64511f653aeaadc80c79cfc74c

@csrf_exempt
def runwayAssignment(request):
    body = json.loads(request.body)
    print(body)
    plane = Plane.objects.get(identifier=body["plane"])
    origin = Airport.objects.get(name=body["origin"])
    dest = Airport.objects.get(name=body["destination"])
    plane.take_off_airport = origin
    plane.land_airport = dest
    plane.runway = Airport.objects.get(name=body["runway"])
    plane.landing_time = body["landing_time"]
    plane.take_off_time = body["take_off_time"]
    plane.save()
    testplane = Plane.objects.get(identifier=plane.identifier)
    duplicategate = find_duplicate_gate(testplane)
    if duplicategate != []:
        duplicates  = duplicategate[0]
        plane1_id = duplicates.identifier
        plane2_id = plane.identifier
        response_body = """
    "team_id": "89ecdb63-8123-4ded-a647-5f7409a9cfc5",
    "obj_type": "Plane",
    "id": "{}",
    "error": "duplicate runway"
    """.format(plane1_id, plane2_id)
    return HttpResponse(response_body)


class GateListView(ListView):
    model = Gate
    template_name = "atc/gate_list.html"
    paginate_by = 20
    context_object_name = "gate_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        super(GateListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(GateListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(GateListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(GateListView, self).get_queryset()

    def get_allow_empty(self):
        return super(GateListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(GateListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(GateListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(GateListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(GateListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(GateListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(GateListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(GateListView, self).get_template_names()


class GateDetailView(DetailView):
    model = Gate
    template_name = "atc/gate_detail.html"
    context_object_name = "gate"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        super(GateDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(GateDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(GateDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(GateDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(GateDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(GateDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(GateDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(GateDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(GateDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(GateDetailView, self).get_template_names()


class GateCreateView(SuperuserRequiredMixin, CreateView):
    model = Gate
    form_class = GateForm
    template_name = "atc/gate_create.html"
    success_url = reverse_lazy("gate_list")

    def __init__(self, **kwargs):
        super(GateCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(GateCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(GateCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(GateCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(GateCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(GateCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(GateCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(GateCreateView, self).get_initial()

    def form_invalid(self, form):
        response = super(GateCreateView, self).form_invalid(form)
        response.status_code = 400
        return response

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(GateCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(GateCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(GateCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(GateCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("atc:gate_detail", args=(self.object.pk,))


class GateUpdateView(SuperuserRequiredMixin, UpdateView):
    model = Gate
    form_class = GateForm
    template_name = "atc/gate_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "gate"

    def __init__(self, **kwargs):
        super(GateUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(GateUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(GateUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(GateUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(GateUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(GateUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(GateUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(GateUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(GateUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(GateUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(GateUpdateView, self).get_initial()

    def form_invalid(self, form):
        response = super(GateUpdateView, self).form_invalid(form)
        response.status_code = 400
        return response

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(GateUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(GateUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(GateUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(GateUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(GateUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("atc:gate_detail", args=(self.object.pk,))


class GateDeleteView(SuperuserRequiredMixin, DeleteView):
    model = Gate
    template_name = "atc/gate_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "gate"

    def __init__(self, **kwargs):
        super(GateDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(GateDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(GateDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(GateDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(GateDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(GateDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(GateDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(GateDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(GateDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(GateDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(GateDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("atc:gate_list")
#>>>>>>> master
