from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('isi-kuesioner/', views.home_kuesioner, name='home_kuesioner'),
    path('cari-alumni/', views.cari_alumni, name='cari_alumni'),
    path('tentang/', views.tentang, name='tentang'),
    path('kontak/', views.kontak, name='kontak'),
    
    
    
    path('backend/home/', views.home, name='home'),
    path('backend/lihat-alumni/', views.lihat_alumni, name='lihat_alumni'),
    
    path('backend/pertanyaan/', views.lihat_pertanyaan, name='lihat_pertanyaan'),
    path('backend/pertanyaan/tambah-pertanyaan/', views.tambah_pertanyaan, name='tambah_pertanyaan'),
    path('backend/pertanyaan/detail-pertanyaan/<detail_id>', views.detail_pertanyaan, name='detail_pertanyaan'),
    path('backend/pertanyaan/update-pertanyaan/<update_id>', views.update_pertanyaan, name='update_pertanyaan'),
    path('backend/pertanyaan/hapus-pertanyaan/<delete_id>', views.hapus_pertanyaan, name='hapus_pertanyaan'),
    
    path('backend/jawaban/', views.lihat_jawaban, name='lihat_jawaban'),
    path('backend/jawaban/tambah-jawaban/', views.tambah_jawaban, name='tambah_jawaban'),
    path('backend/jawaban/update-jawaban/<update_id>', views.update_jawaban, name='update_jawaban'),
    path('backend/jawaban/hapus-jawaban/<delete_id>', views.hapus_jawaban, name='hapus_jawaban'),
    
    path('backend/laporan/', views.lihat_laporan, name='lihat_laporan'),
    path('backend/laporan/tambah-laporan/', views.tambah_laporan, name='tambah_laporan'),
    path('backend/laporan/detail-laporan/<detail_id>', views.detail_laporan, name='detail_laporan'),
    path('backend/laporan/update-laporan/<update_id>', views.update_laporan, name='update_laporan'),
    path('backend/laporan/hapus-laporan/<delete_id>', views.hapus_laporan, name='hapus_laporan'),
    
    path('backend/grafik/', views.lihat_grafik, name='lihat_grafik')
]
