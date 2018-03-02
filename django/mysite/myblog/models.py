# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class TldTplanInfo(models.Model):
    plan_code = models.CharField(primary_key=True, max_length=32)
    plan_name = models.CharField(max_length=100, blank=True, null=True)
    plan_fullname = models.CharField(max_length=200, blank=True, null=True)
    plan_type = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tld_tplan_info'


class TldTportInfo(models.Model):
    port_code = models.CharField(max_length=32)
    port_name = models.CharField(max_length=200, blank=True, null=True)
    port_fullname = models.CharField(max_length=500, blank=True, null=True)
    beg_date = models.CharField(max_length=10, blank=True, null=True)
    end_date = models.CharField(max_length=10, blank=True, null=True)
    port_type = models.CharField(max_length=1, blank=True, null=True)
    plan_code = models.CharField(max_length=32, blank=True, null=True)
    abs_base = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tld_tport_info'

