from django.db import models

# Create your models here.


class RawData(models.Model):
    round = models.IntegerField(unique=True)
    date_local = models.DateField()

    num1 = models.IntegerField()
    num2 = models.IntegerField()
    num3 = models.IntegerField()
    num4 = models.IntegerField()
    num5 = models.IntegerField()
    num6 = models.IntegerField()
    bonus = models.IntegerField()

    first_win = models.IntegerField()
    second_win = models.IntegerField()
    third_win = models.IntegerField()
    fourth_win = models.IntegerField()
    last_win = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        db_table = 'raw_data'
    
        
class Population(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    counts = models.IntegerField()
    season = models.IntegerField()
    depth = models.IntegerField()
    
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    class Meta:
        db_table = 'populations'
        index_together = ['name', 'season']


class UpdateRecord(models.Model):
    last_snyc_date = models.DateField()
    execution_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        db_table = 'update_record'