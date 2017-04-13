from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(StringResource)
admin.site.register(IntResource)
admin.site.register(ListResource)
admin.site.register(DictResource)
admin.site.register(DictResourceEntry)