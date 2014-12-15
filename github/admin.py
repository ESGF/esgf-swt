from django.contrib import admin

from github.models import Group
from github.models import Issue
from github.models import Solution
from github.models import Location
from github.models import Browser
from github.models import Site

admin.site.register(Group)
admin.site.register(Issue)
admin.site.register(Solution)
admin.site.register(Location)
admin.site.register(Browser)
admin.site.register(Site)
