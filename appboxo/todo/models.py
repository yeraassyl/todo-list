from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    def get_todos(self):
        return Todo.objects.filter(category=self.pk)

    def __str__(self):
        return self.title


class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
