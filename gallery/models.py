from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        
    def __str__(self):
        return self.nombre

class Galeria(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.CharField(max_length=200)
    fecha_estreno = models.DateField(verbose_name='Fecha de estreno', null=True, blank=True)
    imagen = models.ImageField(upload_to='galeria', null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, related_name='galerias')
    
    class Meta:
        verbose_name = 'Galeria'
        verbose_name_plural = 'Galerias'
        
    def __str__(self):
        return str(self.title)

class Personaje(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='personajes', null=True, blank=True)
    galeria = models.ForeignKey(Galeria, on_delete=models.CASCADE, related_name='personajes')
    
    class Meta:
        verbose_name = 'Personaje'
        verbose_name_plural = 'Personajes'
        
    def __str__(self):
        return self.nombre

