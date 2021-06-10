from django import forms
from Combi19App.models import Viaje


class CompraPasajeForm(forms.ModelForm):
    class Meta:
        model = Viaje
        fields = ("asientos_ocupados",)

    def clean_asientos_ocupados(self):
        asientos = self.cleaned_data['asientos_ocupados']
        return asientos
