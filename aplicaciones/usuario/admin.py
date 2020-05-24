from django.contrib import admin
from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):   
    search_fields = ['nombre']
    list_display = ('nombre', 'login','usuario',)

admin.site.register(Usuario, UsuarioAdmin)
