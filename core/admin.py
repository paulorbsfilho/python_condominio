from django.contrib import admin

from .models import Apartamento

# Register your models here.



class ApartamentoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Cadastro apartamento',{'fields': ['numero', 'qtdQuartos', 'ocupacao', 'proprietario']})
    ]
    list_display = ('numero', 'qtdQuartos', 'ocupacao', 'proprietario')
    list_filter = ['qtdQuartos', 'ocupacao']
    search_fields = ['numero']

admin.site.register(Apartamento, ApartamentoAdmin)