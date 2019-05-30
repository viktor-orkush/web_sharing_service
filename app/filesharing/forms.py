from django import forms

from filesharing.models import Document


class DocumentForm(forms.Form):
    description = forms.CharField(max_length=255, required=False)
    document = forms.FileField(required=True)
    file_live_day = forms.IntegerField()
    file_live_hour = forms.IntegerField()
    file_live_minute = forms.IntegerField(required=True)