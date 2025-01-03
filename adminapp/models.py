from django.db import models

from django.db import models

class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    addresses = models.ManyToManyField('userapp.Address', through='AddressGroup')

class AddressGroup(models.Model):
    address = models.ForeignKey('userapp.Address', on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
