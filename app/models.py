from django.db import models
from datetime import datetime 

STATUS = (
    (0, "incomplete"),
    (1, "complete")
)


class Todolist(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    created_on = models.DateField(default=datetime.today)
    deadline = models.DateField(auto_now_add=False)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['deadline']
    
    def __str__(self):
        return self.title
