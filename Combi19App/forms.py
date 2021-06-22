from django import forms
from Combi19App.models import Comentario, Viaje


class CompraPasajeForm(forms.ModelForm):
    class Meta:
        model = Viaje
        fields = ("asientos_ocupados",)

    def clean_asientos_ocupados(self):
        asientos = self.cleaned_data['asientos_ocupados']
        return asientos

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ("ruta", "comentario")

    def clean_ruta(self):
        ruta = self.cleaned_data['ruta']
        return ruta

    def clean_comentario(self):
        comentario = self.cleaned_data["comentario"]
        return comentario
    
    def save(self, commit=True):
        comentario = Comentario()
        comentario.usuario = self.instance
        comentario.ruta = self.cleaned_data['ruta']
        comentario.comentario = self.cleaned_data["comentario"]
        if commit:
            comentario.save()
        return comentario
