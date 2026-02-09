from django import forms
from prog_lang.models import ProgLand

class ProgLangForm(forms.ModelForm):
    class Meta:
        model = ProgLand
        fields = "__all__"

        #если вдруг только определенные
        #fields = "title description".split()