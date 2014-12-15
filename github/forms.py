from django import forms
from django.forms.models import modelform_factory 
from github.models import Group, Issue, Solution, Location, Browser, Site, Log 

LogForm = modelform_factory(Log)


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=1024)
    file = forms.FileField()
