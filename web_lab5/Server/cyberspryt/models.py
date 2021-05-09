from django.db import models

class teams(models.Model):
    class Meta:
        ordering = ['id']
        unique_together = ('name', 'discipline','amount')

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    discipline = models.CharField(max_length=50)
    amount = models.IntegerField()



    def __str__(self):
        return self.nameсцици

    def __str__(self):
        return self.discipline