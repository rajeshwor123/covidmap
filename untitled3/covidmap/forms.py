from django import forms
from .models import pandemic


class PatientAdd(forms.ModelForm):
    class Meta:
        model = pandemic
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PatientAdd, self).__init__(*args, **kwargs)
        self.fields['province'].empty_label = "Select"
        self.fields['infected'].required = False
        self.fields['death'].required = False
        self.fields['recovered'].required = False
