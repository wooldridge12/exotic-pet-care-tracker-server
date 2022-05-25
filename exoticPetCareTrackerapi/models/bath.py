from django.db import models

care_taker = models.ForeignKey("CareTaker", on_delete=models.CASCADE)
duration = models.IntegerField()
time = models.TimeField()
notes = models.CharField(max_length=1000)