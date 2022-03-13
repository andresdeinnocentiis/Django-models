from tabnanny import verbose
from django.db import models

# NOTE: Para poder utilizar el modelo "user" que viene por defecto en Django,
# Debemos importarlo previamente:

from django.contrib.auth.models import User

# Create your models here.


class Comic(models.Model):
    '''
    Esta clase hereda de Django models.Model y crea una tabla llamada
    e_commerce_comic. Las columnas toman el nombre especificado de cada objeto.
    '''
    id = models.BigAutoField(db_column='ID', primary_key=True)
    marvel_id = models.PositiveIntegerField(
        verbose_name='marvel ids', default=1, unique=True)
    title = models.CharField(
        verbose_name='titles', max_length=120, default='')
    description = models.TextField(
        verbose_name='descriptions', default='')
    price = models.FloatField(
        verbose_name='prices', max_length=5, default=0.00)
    stock_qty = models.PositiveIntegerField(
        verbose_name='stock qty', default=0)
    picture = models.URLField(
        verbose_name='pictures', default='')

    class Meta:
        '''
        Con "class Meta" podemos definir atributos de nuestras entidades como el nombre de la tabla.
        '''
        db_table = 'e_commerce_comics'

    def __str__(self):
        '''
        La función __str__ cumple la misma función que __repr__ en SQL Alchemy, 
        es lo que retorna cuando llamamos al objeto.
        '''
        return f'{self.id}'
class WishList(models.Model):
    '''
    Esta clase hereda de Django models.Model y crea una tabla llamada
    e_commerce_comic. Las columnas toman el nombre especificado de cada objeto.
    '''
    id = models.BigAutoField(
        db_column='ID', 
        primary_key=True
    )
    user_id = models.ForeignKey(
        to=User, 
        on_delete=models.DO_NOTHING, 
        verbose_name="user ids", 
        default=1
    )
    comic_id = models.ForeignKey(
        to=Comic, 
        on_delete=models.DO_NOTHING, 
        verbose_name="comic ids", 
        default=1, 
        blank=True
    )
    favorite = models.BooleanField(
        verbose_name='favorite', 
        default= True
    )
    cart = models.BooleanField(
        verbose_name='cart', 
        default= True
    )
    wished_qty = models.PositiveIntegerField(
        verbose_name='wished qty', 
        default=0
    )
    bought_qty = models.PositiveIntegerField(
        verbose_name='bought qty', 
        default=0
    )

    class Meta:
        '''
        Con "class Meta" podemos definir atributos de nuestras entidades como el nombre de la tabla.
        '''
        db_table = 'e_commerce_wish_list'

    def __str__(self):
        '''
        La función __str__ cumple la misma función que __repr__ en SQL Alchemy, 
        es lo que retorna cuando llamamos al objeto.
        '''
        return f'{self.id}'