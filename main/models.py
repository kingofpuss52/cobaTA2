from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils import timezone

# Create your models here.

class CustomUser(AbstractUser):
    # ini untuk mengintergrasikan user admin dengan user dari bawaan
    
    is_admin = models.BooleanField(default=False)
    is_alumni = models.BooleanField(default=True)
    
class Pertanyaan(models.Model):
    pilihan = (
        ("Text", "Text"),
        ("Radio", "Radio"),
    )
    
    id = models.AutoField(primary_key=True)
    pertanyaan = models.TextField()
    jenis = models.CharField(choices=pilihan, default='Text', max_length=10)
    
    def __str__(self):
        return self.pertanyaan + "\n" + self.jenis
 
class Jawaban(models.Model):
    pilihan_skor = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
    )
    
    kode_pertanyaan = models.ForeignKey(Pertanyaan, null=True, on_delete=models.SET_NULL, limit_choices_to={'jenis': 'Radio'})
    isi = models.CharField(max_length=200, null=True)
    skor = models.CharField(max_length=1, null=True, choices=pilihan_skor)
    
class Laporan(models.Model):
    id = models.AutoField(primary_key=True)
    file_laporan = models.FileField(upload_to='documents/')
    tanggal_upload = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.file_laporan + "\n" + self.tanggal_upload