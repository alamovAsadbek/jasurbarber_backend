from django.db import models


class Queue(models.Model):
    customer_first_name = models.CharField(max_length=100)
    customer_last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    service = models.CharField(max_length=100)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    date = models.DateTimeField()  # foydalanuvchi kiritadigan sana + soat
    whom = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Queue"
        verbose_name_plural = "Queues"

    def __str__(self):
        return f"{self.customer_first_name} {self.customer_last_name} - {self.service}"
