from django.db import models


class User(models.Model):
    email      = models.EmailField(max_length=200, unique=True, verbose_name='email', null=True)
    password   = models.CharField(max_length=200, null=True)
    first_name = models.CharField(max_length=45, null=True)
    last_name  = models.CharField(max_length=45, null=True)
    create_at  = models.DateTimeField(auto_now_add=True, null=True)
    update_at  = models.DateTimeField(auto_now=True, null=True)
    is_delete  = models.BooleanField(default=False)
    address    = models.ManyToManyField('Address', through='User_address')
    kakao_id   = models.CharField(max_length=250, null=True)

    class Meta:
        db_table = 'users'


class User_address(models.Model):
    address = models.ForeignKey('Address', on_delete=models.CASCADE, null=True)
    user    = models.ForeignKey('User', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'user_addresses'


class Address(models.Model):
    first_name = models.CharField(max_length=45, null=True)
    last_name  = models.CharField(max_length=45, null=True)
    company    = models.CharField(max_length=200, null=True)
    address1   = models.CharField(max_length=200, null=True)
    address2   = models.CharField(max_length=200, null=True)
    city       = models.CharField(max_length=100, null=True)
    country    = models.CharField(max_length=100, null=True)
    state      = models.CharField(max_length=100, null=True)
    phone      = models.CharField(max_length=45, null=True)
    is_default = models.BooleanField(False, null=True)
    postcode   = models.ForeignKey('Postcode', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'addresses'


class Postcode(models.Model):
    postcode      = models.CharField(max_length=45)
    shipping_cost = models.DecimalField(max_digits=8, decimal_places=2, null=True)

    class Meta:
        db_table = 'postcodes'
