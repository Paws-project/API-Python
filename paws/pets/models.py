from django.db import models

petchoises = [
    ["dog", "Dog"],
    ["cat", "Cat"]
]

class Pet(models.Model):
    type = models.CharField(choices=petchoises, max_length=15, verbose_name="Pet type")
    nickname = models.CharField(max_length=30, verbose_name="Pet nickname")
    male = models.BooleanField(verbose_name="Male sex?")
    birth_date = models.DateField(verbose_name="Pet birth date")
    chip_number = models.BigIntegerField(verbose_name="Chip number", null=True)
    chip_implantation_date = models.DateField(verbose_name="Chip implantation date", null=True)

class PetPhoto(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="Pet photo")

class LostPet(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    loss_date = models.DateField(verbose_name="Date of loss")
