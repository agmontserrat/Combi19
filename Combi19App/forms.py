
from django import forms
from Combi19App.models import Comentario, Testeo, Viaje


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

class EditarComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ("ruta", "comentario")
    def clean_ruta(self):
        ruta = self.cleaned_data['ruta']
        return ruta

    def clean_comentario(self):
        comentario = self.cleaned_data["comentario"]
        return comentario

class DatosCovid(forms.ModelForm):
    contador_sintomas=0
    
    class Meta:
        model = Testeo
        fields = ("temperatura","dificultad_respiratoria","tos","dolor_garganta","dolor_cabeza","dolor_muscular","vomitos_diarrea","perdida_gusto_olfato")

    def clean_temperatura(self):
        temperatura = self.cleaned_data['temperatura']
            # if temperatura > 38:
            #     self.contador_sintomas = self.contador_sintomas+1
        return temperatura
    
    def clean_dificultadRespiratoria(self):
        dificultad_respiratoria = self.cleaned_data["dificultad_respiratoria"]
        if dificultad_respiratoria:
            self.contador_sintomas = self.contador_sintomas+1
        return dificultad_respiratoria
    
    def clean_tos(self):
        tos = self.cleaned_data['tos']
        if tos:
            self.contador_sintomas = self.contador_sintomas+1
        return tos
    
    def clean_dolorGarganta(self):
        dolor_garganta = self.cleaned_data['dolor_garganta']
        if dolor_garganta:
            self.contador_sintomas = self.contador_sintomas+1
        return dolor_garganta
    
    def clean_dolorCabeza(self):
        dolor_cabeza = self.cleaned_data['dolor_cabeza']
        if dolor_cabeza:
            self.contador_sintomas = self.contador_sintomas+1
        return dolor_cabeza

    def clean_dolorMuscular(self):
        dolor_muscular = self.cleaned_data['dolor_muscular']
        if dolor_muscular:
            self.contador_sintomas = self.contador_sintomas+1
        return dolor_muscular
    
    def clean_vomitosDiarrea(self):
        vomitos_diarrea = self.cleaned_data['vomitos_diarrea']
        if vomitos_diarrea:
            self.contador_sintomas = self.contador_sintomas+1
        return vomitos_diarrea
    
    def clean_perdidaGustoOlfato(self):
        perdida_gusto_olfato = self.cleaned_data['perdida_gusto_olfato']
        if perdida_gusto_olfato:
            self.contador_sintomas = self.contador_sintomas+1
        return perdida_gusto_olfato

    def save(self, commit=True):
        datos_covid = Testeo()
        datos_covid.usuario = self.instance
        datos_covid.temperatura = self.cleaned_data['temperatura']
        datos_covid.dificultad_respiratoria = self.cleaned_data['dificultad_respiratoria']
        datos_covid.tos = self.cleaned_data['tos']
        datos_covid.dolor_garganta = self.cleaned_data['dolor_garganta']
        datos_covid.dolor_cabeza = self.cleaned_data['dolor_cabeza']
        datos_covid.dolor_muscular = self.cleaned_data['dolor_muscular']
        datos_covid.vomitos_diarrea = self.cleaned_data['vomitos_diarrea']
        datos_covid.perdida_gusto_olfato = self.cleaned_data['perdida_gusto_olfato']
        if commit:
            datos_covid.save()
        return datos_covid