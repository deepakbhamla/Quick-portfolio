from django.contrib import admin
from .models import Profile, Project, Contact, SkillLevel
# Register your models here.
admin.site.site_header = 'The Alankar Shukla'
admin.site.site_title = 'my personal portfolio '
admin.site.index_title = 'my personal portfolio'

admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Contact)
admin.site.register(SkillLevel)
