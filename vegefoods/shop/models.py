from django.db import models



KIND_CHOICES = (
    ('vegetables','Vegetables'),
    ('fruits', 'Fruits'),
    ('juice','Juice'),
    ('dried','Dried'),
)
class Vegtables(models.Model):
    title = models.CharField(max_length=255, unique=True)
    kind = models.CharField(max_length=10, choices=KIND_CHOICES, default='green')
    prise = models.DecimalField(max_digits=6, decimal_places=2)
    Discount = models.PositiveIntegerField(default=0)
    detail = models.TextField(blank=True, default='')
    count = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to = 'static/media/vegtables', default = 'static/media/vegtables/no-img.jpg')

    def __str__(self):
        return self.title

    def discount_prise(self):
        return (self.prise * (100 - self.Discount))/100

    class Meta:
        ordering = ["title"]
