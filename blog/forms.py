from django import forms


class DiaryForm(forms.Form):
    name = forms.CharField(max_length=50)