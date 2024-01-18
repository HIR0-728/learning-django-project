import re
from django.db import models


# Create your models here.
class Person(models.Model):
    first_name = models.CharField("名", max_length=30)
    last_name = models.CharField("姓", max_length=30)
    age = models.IntegerField("年齢")
    nickname = models.CharField("ニックネーム", max_length=255, blank=True)
    created_at = models.DateTimeField("作成日時", auto_now_add=True)
    updated_at = models.DateTimeField("更新日時", auto_now=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Organization(models.Model):
    name = models.CharField("組織名", max_length=255)
    person = models.ForeignKey(
        Person, verbose_name="人", related_name="organizations", on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.name
