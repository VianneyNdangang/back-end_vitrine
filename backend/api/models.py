from importlib.metadata import requires

from django.db import models

# Create your models here.
class Project(models.Model):
    id = models.BigAutoField(primary_key=True , editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        db_table = 'projects'
        ordering = ['date']

    def __str__(self):
        return f'{self.title}'

class Service(models.Model):
    id = models.BigAutoField(primary_key=True , editable=False)
    name = models.TextField()
    image = models.ImageField(upload_to='services/', blank=True, null=True)

    class Meta:
        db_table = 'services'
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'

class Reviews(models.Model):
    id = models.BigAutoField(primary_key=True , editable=False)
    username = models.CharField(max_length=50)
    company = models.CharField(max_length=50, blank=True, null=True)
    notation = models.PositiveIntegerField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        ordering = ['created_at']
        db_table = 'reviews'

    def __str__(self):
        return f'{self.username}'
