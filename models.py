from django.db import models

# Create your models here.
class Perreria(models.Model):

    id = models.AutoField(primary_key=True)
    nombre_del_perro = models.CharField(max_length=60)
    raza = models.CharField(max_length=100)
    tamaño  = models.CharField(max_length=50)
    foto = models.ImageField(
        upload_to = 'foto/%Y/%m/%d',
        blank = True,
        verbose_name = ('Foto del perro')
    )

class Meta:
    verbose_name = ('Perreria')
    verbose_name_plural = ('Perreria')

def __str__(self):
    return self.nombre