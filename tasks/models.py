from django.db import models

# Create Task model consists of two fields text for storing item text and the done for the state of the task

class Task(models.Model):
    text = models.CharField(max_length=50)
    done = models.BooleanField(default=False)

    #overwrite default __str__ method to return the object with content name
    def __str__(self):
        return self.text