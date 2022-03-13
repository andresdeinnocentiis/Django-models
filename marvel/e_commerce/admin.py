from django.contrib import admin

# NOTE: Tenemos que importar los modelos con los que vamos a trabajar:
from e_commerce.models import *

# Register your models here.

# NOTE: Aquí personalizamos los campos en el Django Admin.

@admin.register(Comic)
class ComicsAdmin(admin.ModelAdmin):
    # NOTE: Para seleccionar los campos en la tabla de registros
    list_display = ('marvel_id', 'title', 'stock_qty', 'price') # Nombres de las columnas que quiero mostrar

    # NOTE: Filtro lateral de elementos:
    list_filter= ('marvel_id','title')
    
    # NOTE: Buscador de elementos en la columna:
    search_fields = ['title']

    # NOTE: Para seleccionar los campos en el registro. 
    # # SE PUEDE USAR ESTE o FIELDSETS, NO AMBOS.
    #fields = ('marvel_id', 'title', 'description', 'stock_qty', 'price')

    # NOTE: Genera un campo desplegable con los registros seleccionados.
    # SE PUEDE USAR ESTE o FIELD, NO AMBOS.
    fieldsets = (
        (None, {
            'fields': ('marvel_id', 'title', 'stock_qty')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('description','price', 'picture'),
        }),
    )
    pass
@admin.register(WishList)
class WishListsAdmin(admin.ModelAdmin):
    # NOTE: Para seleccionar los campos en la tabla de registros
    list_display = ('user_id', 'comic_id', 'favorite', 'cart', 'wished_qty', 'bought_qty') # Nombres de las columnas que quiero mostrar

    # NOTE: Filtro lateral de elementos:
    list_filter= ('user_id','comic_id')
    
    # NOTE: Buscador de elementos en la columna:
    search_fields = ['user_id', 'comic_id']

    # NOTE: Para seleccionar los campos en el registro. 
    # # SE PUEDE USAR ESTE o FIELDSETS, NO AMBOS.
    #fields = ('marvel_id', 'title', 'description', 'stock_qty', 'price')

    # NOTE: Genera un campo desplegable con los registros seleccionados.
    # SE PUEDE USAR ESTE o FIELD, NO AMBOS.
    fieldsets = (
        (None, {
            'fields': ('user_id', 'comic_id', 'wished_qty')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('favorite','cart', 'bought_qty'),
        }),
    )
    pass