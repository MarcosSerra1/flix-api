from django.contrib import admin
from actors.models import Actors


@admin.register(Actors)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'birthday', 'nationality')
