from django.db import models

class Food(models.Model):
    # care_taker = models.ForeignKey("CareTaker", on_delete=models.CASCADE)
    time = models.TimeField()
    Quantity = models.IntegerField()
    food = models.ForeignKey("FoodType", on_delete=models.CASCADE)
    