from django import forms
class HacerPedidoFormulario(forms.Form):
    tipo=forms.CharField(max_length=30)
    descripcion=forms.CharField()
    costo=forms.IntegerField()
    cantidad=forms.IntegerField()