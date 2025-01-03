from django.db import models

from django.db import models

class Address(models.Model):
    address_id = models.BigAutoField(primary_key=True)
    full_name = models.CharField(max_length=255, null=True)
    nickname = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True)
    company = models.CharField(max_length=255, null=True)
    department = models.CharField(max_length=255, null=True)
    job_title = models.CharField(max_length=255, null=True)
    street = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    zip_code = models.CharField(max_length=255, null=True)
    facebook_link = models.CharField(max_length=255, null=True)
    instagram_link = models.CharField(max_length=255, null=True)
    linkedin_link = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
