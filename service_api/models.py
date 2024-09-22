from django.db import models

# Create your models here.
class Pengukuran(models.Model):
    suhu_air = models.FloatField()
    ph = models.FloatField()
    total_solid_dissolve = models.FloatField(null=True)
    waktu_pengukuran = models.DateTimeField(auto_now_add=True)



class Konfigurasi(models.Model):
    nama_konfigurasi = models.CharField(max_length=55)
    nilai = models.FloatField()
