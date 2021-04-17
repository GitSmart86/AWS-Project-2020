from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Airline
from ..forms import AirlineForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404
from braces.views import SuperuserRequiredMixin


class AirlineListView(ListView):
    model = Airline
    template_name = "atc/airline_list.html"
    paginate_by = 20
    context_object_name = "airline_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        super(AirlineListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AirlineListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AirlineListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(AirlineListView, self).get_queryset()

    def get_allow_empty(self):
        return super(AirlineListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(AirlineListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(AirlineListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(AirlineListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(AirlineListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(AirlineListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(AirlineListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AirlineListView, self).get_template_names()


class AirlineDetailView(DetailView):
    model = Airline
    template_name = "atc/airline_detail.html"
    context_object_name = "airline"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        super(AirlineDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AirlineDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AirlineDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(AirlineDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(AirlineDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(AirlineDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(AirlineDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(AirlineDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(AirlineDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AirlineDetailView, self).get_template_names()


class AirlineCreateView(SuperuserRequiredMixin, CreateView):
    model = Airline
    form_class = AirlineForm
    template_name = "atc/airline_create.html"
    success_url = reverse_lazy("airline_list")

    def __init__(self, **kwargs):
        super(AirlineCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(AirlineCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AirlineCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(AirlineCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(AirlineCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(AirlineCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(AirlineCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(AirlineCreateView, self).get_initial()

    def form_invalid(self, form):
        response = super(AirlineCreateView, self).form_invalid(form)
        response.status_code = 400
        return response

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(AirlineCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(AirlineCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(AirlineCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AirlineCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("atc:airline_detail", args=(self.object.pk,))


class AirlineUpdateView(SuperuserRequiredMixin, UpdateView):
    model = Airline
    form_class = AirlineForm
    template_name = "atc/airline_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "airline"

    def __init__(self, **kwargs):
        super(AirlineUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AirlineUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AirlineUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(AirlineUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(AirlineUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(AirlineUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(AirlineUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(AirlineUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(AirlineUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(AirlineUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(AirlineUpdateView, self).get_initial()

    def form_invalid(self, form):
        response = super(AirlineUpdateView, self).form_invalid(form)
        response.status_code = 400
        return response

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(AirlineUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(AirlineUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(AirlineUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(AirlineUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AirlineUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("atc:airline_detail", args=(self.object.pk,))


class AirlineDeleteView(SuperuserRequiredMixin, DeleteView):
    model = Airline
    template_name = "atc/airline_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "airline"

    def __init__(self, **kwargs):
        super(AirlineDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AirlineDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(AirlineDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(AirlineDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(AirlineDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(AirlineDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(AirlineDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(AirlineDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(AirlineDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(AirlineDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AirlineDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("atc:airline_list")
