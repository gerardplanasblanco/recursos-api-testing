from django.contrib import admin
from .models import Autor, Recurs


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nom', 'cognoms', 'email', 'carrec')
    search_fields = ('nom', 'cognoms', 'email')


@admin.register(Recurs)
class RecursAdmin(admin.ModelAdmin):
    list_display = ('titol', 'categoria', 'autor', 'data_publicacio', 'is_active')
    list_filter = ('categoria', 'is_active')
    search_fields = ('titol', 'descripcio', 'autor__nom', 'autor__cognoms')
