from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=128)
    short_name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отделение'
        verbose_name_plural = 'Отделения'

class Technics(models.Model):
    name = models.CharField(max_length=128)
    t_type = models.ForeignKey('Type',on_delete = models.CASCADE, related_name = 'Тип')
    serial = models.IntegerField(default = 0)
    depart = models.ForeignKey('Department',on_delete=models.CASCADE,related_name = 'Отделение',default = None, blank = True)
    writeoff = models.BooleanField(blank = True, default = False)
    busy = models.BooleanField(blank = True, default = False)


    def __str__(self):
        return self.name + " | " + self.depart.short_name + " | " + str(self.serial)
    class Meta:
        verbose_name = 'Техника'
        verbose_name_plural = 'Техника'

class SendRecord(models.Model):
    technics = models.ForeignKey('Technics',on_delete=models.CASCADE,related_name='Техника')
    get_date = models.DateField(blank = True,null=True)
    send_date = models.DateField(blank = True,null=True)
    retus_date = models.DateField(blank = True,null=True)
    ret_date = models.DateField(blank = True,null=True)
    repair_reason = models.CharField(max_length=500,blank = True,null=True)
    done = models.BooleanField(blank = True, default = False)

class Type(models.Model):
    name = models.CharField(max_length = 128)

    def __str__(self):
        return self.name
