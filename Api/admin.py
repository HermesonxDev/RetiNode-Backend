from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Discussions)
admin.site.register(Logs)
admin.site.register(Comments)