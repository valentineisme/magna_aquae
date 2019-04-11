from django.contrib import admin
from models.user import Usuario
from models.bacia_hidrografica import Bacia_Hidrografica
from models.rio import Rio
from models.ponto_monitoramento import Ponto_Monitoramento
from models.casos import Casos
# Register your models here.
admin.site.register(Bacia_Hidrografica)
admin.site.register(Rio)
admin.site.register(Usuario)
admin.site.register(Ponto_Monitoramento)
admin.site.register(Casos)