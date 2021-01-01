from django.db import models

petchoises = [
    ["dog", "Dog"],
    ["cat", "Cat"]
]

class Pet(models.Model):
    pet_type = models.CharField(choices=petchoises, max_length=15, verbose_name="Pet type")
    nickname = models.CharField(max_length=30, verbose_name="Pet nickname")
    sex = models.BooleanField(verbose_name="Sex")
    birth_date = models.DateField(verbose_name="Pet birth date")
    chip_number = models.BigIntegerField(verbose_name="Chip number")
    chip_implantation_date = models.DateField(verbose_name="Chip implantation date")
