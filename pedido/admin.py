from django.contrib import admin
from . import models

class ItemPedidoInLine(admin.TabularInline):
    model = models.ItemPedido
    extra: 1

class PedidoAdmin(admin.ModelAdmin):
    inLines = [
        ItemPedidoInLine
    ]
        
admin.site.register(models.Pedido, PedidoAdmin)
admin.site.register(models.ItemPedido)

