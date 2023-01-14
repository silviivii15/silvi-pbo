from django.db import models

class Peminjam(models.Model):
  pilih_keterangan = {
    ('Meminjam'),
    ('Mengembalikan'),
  }
  No = models.IntegerField(null=True)
  Tanggal_Pinjam = models.DateTimeField(auto_now=True)
  Nama_Peminjam = models.CharField(max_length=50)
  Kelas = models.CharField(max_length=20)
  Judul_Buku_dipinjam =models.CharField(max_length=50)
  Banyak_Buku_dipinjam = models.CharField(max_length=50)
  Tanggal_Kembali = models.DateTimeField(max_length=50)
  