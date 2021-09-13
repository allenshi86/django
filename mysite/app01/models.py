from django.db import models

# Create your models here.

class Assets(models.Model):
    AUTHOR_ITEMS = [
        ('0', '永久授权'),
        ('1', '非永久授权'),
    ]

    vendor = models.CharField(max_length=80, verbose_name='vendor')
    soft_name = models.CharField(max_length=60, verbose_name='soft_name')
    dep = models.CharField(max_length=60, verbose_name='预算部门')
    pur_num = models.IntegerField(verbose_name='pur_num')
    autho_type = models.CharField(choices=AUTHOR_ITEMS, max_length=100, verbose_name='autho_type')
    pur_date = models.DateField(editable=True, verbose_name='pur_date')
    expired_date = models.DateField(editable=True, blank=True, null=True, verbose_name='expired_date')
    demander = models.CharField(max_length=60, null=True, blank=True, verbose_name='demander')

    def __str__(self):
        return "%s, %s, %s, %d, %s, %s, %s, %s" % (self.vendor, self.soft_name, self.dep, self.pur_num, self.autho_type, self.pur_date, self.expired_date, self.demander)





