from django.db import models


class Topics(models.Model):
    name = models.CharField(max_length=50, primary_key=True)

    class Meta:
        verbose_name = "Topic"
        verbose_name_plural = "Topics"

    def __str__(self):
        return self.name


class Recipes(models.Model):
    title = models.CharField(max_length=50, primary_key=True)
    image = models.ImageField(upload_to="images")
    description = models.TextField()
    ingredients = models.TextField()
    directions = models.TextField()
    servings = models.IntegerField()
    time = models.IntegerField()
    calories = models.IntegerField()
    fat = models.IntegerField()
    carbs = models.IntegerField()
    protein = models.IntegerField()
    topic = models.ForeignKey(
        Topics, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Recipe"
        verbose_name_plural = "Recipes"

    def __str__(self):
        return self.title
