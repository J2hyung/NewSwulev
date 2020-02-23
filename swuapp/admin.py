from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(User)
admin.site.register(Lecture)
admin.site.register(UserLecture)
admin.site.register(Board)