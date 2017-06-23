from django.db import models


class College(models.Model):
    college_name=models.CharField(max_length=100)
    state=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    Tier_choices=(
        (1, 'first'),
        (2, 'second'),
        (3, 'third'),
        (4, 'other'),
    )
    tier=models.IntegerField(choices=Tier_choices,default=1)

    def __str__(self):
        return self.college_name


class Details(models.Model):
    name=models.ForeignKey(College,on_delete=models.CASCADE)
    annualFee=models.IntegerField()
    officialSite=models.CharField(max_length=1000)

    def __str__(self):
        return self.name

