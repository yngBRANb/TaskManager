from django.db import models

STATUS_CHOICES = (
    ('active', 'Active'),
    ('inactive', 'Inactive'),
    ('archive','Archive'),
)

class Task(models.Model):
    name = models.CharField(verbose_name="Название задачи", max_length=100)
    desc = models.TextField(verbose_name="Описание задачи")
    date_to = models.DateTimeField(verbose_name="До скольки выполнить?")
    time_register = models.DateTimeField(auto_now_add=True)
    status = models.CharField(verbose_name="Статус задачи", choices=STATUS_CHOICES , default='active', max_length=20)  
    
    def __str__(self):
        return self.name
    