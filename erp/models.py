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
    stock = models.IntegerField()
    goods_color = models.CharField(max_length=32)
    goods_size = models.CharField(max_length=4)
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(auto_now=True)


class Inbound(models.Model):
    class Meta:
        db_table = 'inbound'

    in_id = models.AutoField(primary_key=True)
    goods_id = models.ForeignKey(Stuff, on_delete=models.CASCADE)
    count = models.IntegerField()
    inbound_time = models.DateTimeField(default=timezone.now())


class Outbound(models.Model):
    class Meta:
        db_table = 'outbound'

    out_id = models.AutoField(primary_key=True)
    goods_id = models.ForeignKey(Stuff, on_delete=models.CASCADE)
    count = models.IntegerField()
    outbound_time = models.DateTimeField(default=timezone.now())

