from django.contrib import admin

from exercises.models import Doctor, Plan, Exercise

admin.site.register(Doctor)
admin.site.register(Plan)
admin.site.register(Exercise)
