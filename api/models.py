from django.db import models

class BankDetail(models.Model):
    ifsc = models.CharField(max_length=13, null=False, blank=False)
    bank_id = models.IntegerField()
    branch = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=70)
    state = models.CharField(max_length=31)
    bank_name = models.CharField(max_length=70)

    def __str__(self):
        return self.ifsc
