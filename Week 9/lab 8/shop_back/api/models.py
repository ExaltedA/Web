from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=300)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.FloatField()
    description = models.TextField()
    count = models.IntegerField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'count': self.count,
            'category': self.category_id_id,
        }
