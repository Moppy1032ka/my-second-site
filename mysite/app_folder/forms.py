from django import forms

from .models import SampleDB, Document

class SampleForm(forms.ModelForm):

    class Meta:
        model = SampleDB
        fields = ('sample1', 'sample2',)

class DocumentForm(forms.ModelForm):
    
    class Meta:
        model = Document
        fields = ('description', 'document')
