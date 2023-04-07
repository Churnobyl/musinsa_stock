from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.models import UserModel
from django.utils import timezone


class Stuff(models.Model):
    class Meta:
        db_table = 'stuff'

    goods = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    goods_name = models.CharField(max_length=32)
    goods_category = models.CharField(max_length=32)
    goods_color = models.CharField(max_length=32)

    sizes = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('F', 'Free'),
    )

    goods_size = models.CharField(choices=sizes, max_length=1)
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(auto_now=True)
    image = models.CharField(max_length=256)

    def __str__(self):
        return str(self.goods)


class History(models.Model):
    class Meta:
        db_table = 'history'

    sets = (
        ('I', '입고'),
        ('O', '출고'),
        ('N', '신규'),
    )

    history = models.AutoField(primary_key=True)
    in_out = models.CharField(choices=sets, max_length=1)
    goods = models.ForeignKey(Stuff, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    history_time = models.DateTimeField(default=timezone.localtime())

    def __str__(self):
        return str(self.goods)


class Inventory(models.Model):
    class Meta:
        db_table = 'inventory'

    inventory = models.OneToOneField(Stuff, on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)

