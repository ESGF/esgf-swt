from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.forms.models import model_to_dict
from django.forms.util import ErrorList
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.core.files import File

import json
import simplejson
import os
import urllib
import urllib2
import base64
import time
import datetime


from github.models import Group, Issue, Solution, Location, Browser, Site, Log
from github.forms import LogForm

##### General
def render_template(request, template, context):
    template = loader.get_template(template)
    context = RequestContext(request, context)
    return template.render(context)

def not_done(request, *args, **kwargs):
    return HttpResponse("Stub")

##### Index
def index(request):
    form = LogForm()
    return HttpResponse(render_template(request, "github/home.html", {"form":form}))

