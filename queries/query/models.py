
""" Author: Sachin Kafle
    pc: DESKTOP-D9260TN (Workgroup)
    GitHub OpenSource Project (Hosted by Sachin Kafle and Hussen Al Rubaye --Preety Printed (Microsoft Valuable Instructor))

    Author of Book: Learning Python by Building Games

    https://www.amazon.com/Learning-Python-Building-Games-programming/dp/1789802989/ref=sr_1_1?crid=1EL1LTU6SS1QV&keywords=learning+python+by+building+games&qid=1577373614&sprefix=learning+pytho%2Caps%2C445&sr=8-1

    Udemy: https://www.udemy.com/user/6bb6c14f-f5f8-4c0b-b9ca-00c83bb6286c/

 """

from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    date_created = models.DateField() 

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=20)
    creator = models.CharField(max_length=20)
    paradigm = models.CharField(max_length=20)
    date_created = models.DateField()

    def __str__(self):
        return self.name

class Programmer(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return self.name
        