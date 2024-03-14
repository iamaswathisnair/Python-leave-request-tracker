from django.contrib import admin
from . models import Employe,leave,complaint

# Register your models here.


admin.site.register(Employe)
admin.site.register(leave)
admin.site.register(complaint)