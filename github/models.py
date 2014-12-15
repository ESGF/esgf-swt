from django.db import models

# Create your models here.
class Group(models.Model):
    abbreviation = models.CharField(max_length=15, unique=True, blank=False)
    name = models.CharField(max_length=512, unique=True, blank=False)
    email = models.EmailField(max_length=512, unique=True, blank=False)
    issue_name = models.CharField(max_length=1024, unique=True, blank=True)
    github =  models.URLField(max_length=1024, unique=False, blank=True)
    poc =  models.EmailField(max_length=512, unique=False, blank=True)
    def __str__(self):
        return self.name

class Issue(models.Model):
    group_id = models.ForeignKey('Group',unique=False, blank=False)
    text = models.CharField(max_length=1024, unique=True, blank=False)
    solution = models.ForeignKey('Solution',unique=False, blank=True, null=True)
    def __str__(self):
        return self.text

class Solution(models.Model):
    solution =  models.CharField(max_length=4096, unique=True, blank=False)
    def __str__(self):
        return self.solution

class Location(models.Model):
    location = models.CharField(max_length=128, unique=True, blank=False)
    def __str__(self):
        return self.location

class Browser(models.Model):
    browser = models.CharField(max_length=128, unique=True, blank=False)
    def __str__(self):
        return self.browser

class Site(models.Model):
    organization = models.CharField(max_length=128, unique=True, blank=False)
    url = models.URLField(max_length=1024, unique=True, blank=False)
    poc =  models.EmailField(max_length=512, unique=False, blank=True)
    def __str__(self):
        return self.organization

class Log(models.Model):
    group_id = models.ForeignKey('Group',unique=False, blank=False)
    issue_id = models.ForeignKey('Issue',unique=False, blank=False)
    location_id = models.ForeignKey('Location',unique=False, blank=False)
    browser_id = models.ForeignKey('Browser',unique=False, blank=False)
    site_id = models.ForeignKey('Site',unique=False, blank=False)
    comment = models.CharField(max_length=4096, unique=True, blank=False)
    def __str__(self):
        return self.comment
