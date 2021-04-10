from django.contrib import admin
from .models import *

admin.site.site_header = 'Neighborhood Admin'
admin.site.site_title = 'Neighborhood Admin Area'
admin.site.index_title = 'Welcome to Neighborhood admin area'

admin.site.register(Profile)
admin.site.register(Neighbourhood)
admin.site.register(Business)
admin.site.register(Post)