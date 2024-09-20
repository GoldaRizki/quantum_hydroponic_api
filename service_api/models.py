from django.db import models

# Create your models here.
class Pengukuran(models.Model):
    total_solid_dissolve = models.FloatField()
    waktu_pengukuran = models.DateTimeField(auto_now_add=True)



class Konfigurasi(models.Model):
    nama_konfigurasi = models.CharField(max_length=55)
    nilai = models.FloatField()
