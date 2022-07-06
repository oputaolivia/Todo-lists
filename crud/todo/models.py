from django.db import models

# Creating the TodoApp model
class TodoApp(models.Model):
    #Fields of the model
    title = models.CharField(max_length= 200)
    description = models.TextField()

    #rename instances
    def __str__(self):
        return self.title
