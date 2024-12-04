from django import forms
from .models import Contato

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ["nome", "email", "telefone", "mensagem"]
        widgets = {
            "mensagem": forms.Textarea(attrs={"rows": 5}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.fields:
            self.fields['telefone'].widget.attrs.update({'class': 'celular'})