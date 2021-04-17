from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Airport
from ..forms import AirportForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404
from braces.views import SuperuserRequiredMixin


class AirportListView(ListView):
    model = Airport
    template_name = "atc/airport_list.html"
    paginate_by = 20
    context_object_name = "airport_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        super(AirportListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AirportListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AirportListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(AirportListView, self).get_queryset()

    def get_allow_empty(self):
        return super(AirportListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(AirportListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(AirportListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(AirportListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(AirportListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(AirportListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(AirportListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AirportListView, self).get_template_names()


class AirportDetailView(DetailView):
    model = Airport
    template_name = "atc/airport_detail.html"
    context_object_name = "airport"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        super(AirportDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AirportDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AirportDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(AirportDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(AirportDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(AirportDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(AirportDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(AirportDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(AirportDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AirportDetailView, self).get_template_names()


class AirportCreateView(SuperuserRequiredMixin, CreateView):
    model = Airport
    form_class = AirportForm
    template_name = "atc/airport_create.html"
    success_url = reverse_lazy("airport_list")

    def __init__(self, **kwargs):
        super(AirportCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(AirportCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AirportCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(AirportCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(AirportCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(AirportCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(AirportCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(AirportCreateView, self).get_initial()

    def form_invalid(self, form):
        response = super(AirportCreateView, self).form_invalid(form)
        response.status_code = 400
        return response

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(AirportCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(AirportCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(AirportCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AirportCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("atc:airport_detail", args=(self.object.pk,))


class AirportUpdateView(SuperuserRequiredMixin, UpdateView):
    model = Airport
    form_class = AirportForm
    template_name = "atc/airport_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "airport"

    def __init__(self, **kwargs):
        super(AirportUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AirportUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AirportUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(AirportUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(AirportUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(AirportUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(AirportUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(AirportUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(AirportUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(AirportUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(AirportUpdateView, self).get_initial()

    def form_invalid(self, form):
        response = super(AirportUpdateView, self).form_invalid(form)
        response.status_code = 400
        return response

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(AirportUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(AirportUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(AirportUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(AirportUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AirportUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("atc:airport_detail", args=(self.object.pk,))


class AirportDeleteView(SuperuserRequiredMixin, DeleteView):
    model = Airport
    template_name = "atc/airport_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "airport"

    def __init__(self, **kwargs):
        super(AirportDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AirportDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(AirportDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(AirportDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(AirportDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(AirportDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(AirportDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(AirportDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(AirportDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(AirportDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AirportDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("atc:airport_list")
