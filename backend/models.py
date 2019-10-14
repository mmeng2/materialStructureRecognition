# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Projectlist(models.Model):
    id = models.CharField(primary_key=True, max_length=200)
    projectname = models.CharField(db_column='projectName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    uploadtime = models.DateTimeField(db_column='uploadTime', blank=True, null=True)  # Field name made lowercase.
    textfilename = models.CharField(db_column='textFileName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(max_length=200, blank=True, null=True)
    isrecognized = models.IntegerField(db_column='isRecognized')  # Field name made lowercase.
    element = models.CharField(max_length=50, blank=True, null=True)
    e = models.CharField(max_length=50, blank=True, null=True)
    bz1 = models.CharField(max_length=50, blank=True, null=True)
    bz2 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'projectlist'

