from django.contrib import admin
from rango.models import Sport, UserProfile,Athlete

class SportAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
class AthleteAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

# Register your models here.
admin.site.register(Sport, SportAdmin)
admin.site.register(Athlete, AthleteAdmin)
admin.site.register(UserProfile)