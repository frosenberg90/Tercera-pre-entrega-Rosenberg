from django import forms
from ckeditor.fields import RichTextFormField

class BaseFormulario(forms.Form):
    tipo=forms.CharField(max_length=30)
    descripcion=RichTextFormField()
    costo=forms.IntegerField()
    cantidad=forms.IntegerField()
    fecha=forms.DateField()
class HacerPedidoFormulario(BaseFormulario):
    ...
    
class ActualizarFormulario(BaseFormulario):
    ...       