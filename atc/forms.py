from django import forms
from .models import Airline, Airport, Gate, Runway, Plane
from django.forms import ModelMultipleChoiceField


class AirlineForm(forms.ModelForm):

    class Meta:
        model = Airline
        fields = ['name', 'airports']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    airports = ModelMultipleChoiceField(required=False, queryset=Airport.objects.all())

    def __init__(self, *args, **kwargs):
        if kwargs.get('instance'):
            initial = kwargs.setdefault('initial', {})
            initial['airports'] = [t.pk for t in kwargs['instance'].airport_set.all()]
        super(AirlineForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(AirlineForm, self).is_valid()

    def full_clean(self):
        return super(AirlineForm, self).full_clean()

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean(self):
        return super(AirlineForm, self).clean()

    def validate_unique(self):
        return super(AirlineForm, self).validate_unique()

    def save(self, commit=True):
        instance = super(AirlineForm, self).save(commit)

        # Prepare a 'save_m2m' method for the form,
        old_save_m2m = self.save_m2m

        def save_m2m():
            old_save_m2m()
            # This is where we actually link the pizza with toppings
            instance.airport_set.clear()
            instance.airport_set.add(*self.cleaned_data['airports'])

        self.save_m2m = save_m2m

        # Do we need to save all changes now?
        if commit:
            instance.save()
            self.save_m2m()

        return instance


class AirportForm(forms.ModelForm):

    class Meta:
        model = Airport
        fields = ['name', 'x', 'y', 'airlines']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    airlines = ModelMultipleChoiceField(required=False, queryset=Airline.objects.all())

    def __init__(self, *args, **kwargs):
        if kwargs.get('instance'):
            initial = kwargs.setdefault('initial', {})
            initial['airlines'] = [t.pk for t in kwargs['instance'].airlines.all()]
        super(AirportForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(AirportForm, self).is_valid()

    def full_clean(self):
        return super(AirportForm, self).full_clean()

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_x(self):
        x = self.cleaned_data.get("x", None)
        return x

    def clean_y(self):
        y = self.cleaned_data.get("y", None)
        return y

    def clean(self):
        return super(AirportForm, self).clean()

    def validate_unique(self):
        return super(AirportForm, self).validate_unique()

    def save(self, commit=True):
        instance = super(AirportForm, self).save(commit)

        # Prepare a 'save_m2m' method for the form,
        old_save_m2m = self.save_m2m

        def save_m2m():
            old_save_m2m()
            # This is where we actually link the pizza with toppings
            instance.airlines.clear()
            instance.airlines.add(*self.cleaned_data['airlines'])

        self.save_m2m = save_m2m

        # Do we need to save all changes now?
        if commit:
            instance.save()
            self.save_m2m()

        return instance


class GateForm(forms.ModelForm):

    class Meta:
        model = Gate
        fields = ['identifier', 'size', 'airport']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(GateForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(GateForm, self).is_valid()

    def full_clean(self):
        return super(GateForm, self).full_clean()

    def clean_identifier(self):
        identifier = self.cleaned_data.get("identifier", None)
        return identifier

    def clean_size(self):
        size = self.cleaned_data.get("size", None)
        return size

    def clean_airport(self):
        airport = self.cleaned_data.get("airport", None)
        return airport

    def clean(self):
        return super(GateForm, self).clean()

    def validate_unique(self):
        return super(GateForm, self).validate_unique()

    def save(self, commit=True):
        return super(GateForm, self).save(commit)


class RunwayForm(forms.ModelForm):

    class Meta:
        model = Runway
        fields = ['identifier', 'size', 'airport']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(RunwayForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(RunwayForm, self).is_valid()

    def full_clean(self):
        return super(RunwayForm, self).full_clean()

    def clean_identifier(self):
        identifier = self.cleaned_data.get("identifier", None)
        return identifier

    def clean_size(self):
        size = self.cleaned_data.get("size", None)
        return size

    def clean_airport(self):
        airport = self.cleaned_data.get("airport", None)
        return airport

    def clean(self):
        return super(RunwayForm, self).clean()

    def validate_unique(self):
        return super(RunwayForm, self).validate_unique()

    def save(self, commit=True):
        return super(RunwayForm, self).save(commit)


class PlaneForm(forms.ModelForm):

    class Meta:
        model = Plane
        fields = ["identifier", "size", "airline", "gate", "runway", "maxPassengerCount", "currentPassengerCount"]
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(PlaneForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(PlaneForm, self).is_valid()

    def full_clean(self):
        return super(PlaneForm, self).full_clean()

    def clean_identifier(self):
        identifier = self.cleaned_data.get("identifier", None)
        return identifier

    def clean_size(self):
        size = self.cleaned_data.get("size", None)
        return size

    def clean_currentPassengerCount(self):
        currentPassengerCount = self.cleaned_data.get("currentPassengerCount", None)
        return currentPassengerCount

    def clean_maxPassengerCount(self):
        maxPassengerCount = self.cleaned_data.get("maxPassengerCount", None)
        return maxPassengerCount

    def clean_airline(self):
        airline = self.cleaned_data.get("airline", None)
        return airline

    def clean_gate(self):
        gate = self.cleaned_data.get("gate", None)
        return gate

    def clean_runway(self):
        runway = self.cleaned_data.get("runway", None)
        return runway

    def clean_take_off_airport(self):
        take_off_airport = self.cleaned_data.get("take_off_airport", None)
        return take_off_airport

    def clean_land_airport(self):
        land_airport = self.cleaned_data.get("land_airport", None)
        return land_airport

    def clean_heading(self):
        heading = self.cleaned_data.get("heading", None)
        return heading

    def clean_speed(self):
        speed = self.cleaned_data.get("speed", None)
        return speed

    def clean_take_off_time(self):
        take_off_time = self.cleaned_data.get("take_off_time", None)
        return take_off_time

    def clean_landing_time(self):
        landing_time = self.cleaned_data.get("landing_time", None)
        return landing_time

    def clean_arrive_at_gate_time(self):
        arrive_at_gate_time = self.cleaned_data.get("arrive_at_gate_time", None)
        return arrive_at_gate_time

    def clean_arrive_at_runway_time(self):
        arrive_at_runway_time = self.cleaned_data.get("arrive_at_runway_time", None)
        return arrive_at_runway_time

    def clean(self):
        return super(PlaneForm, self).clean()

    def validate_unique(self):
        return super(PlaneForm, self).validate_unique()

    def save(self, commit=True):
        return super(PlaneForm, self).save(commit)

    def process_perms(self, request):
        if request != None:
            if request.user.is_staff and not request.user.is_superuser:
                del self.fields["identifier"]
                del self.fields["size"]
                del self.fields["airline"]
                del self.fields["gate"]
                del self.fields["runway"]
                del self.fields["maxPassengerCount"]

