from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import PertanyaanForm, JawabanForm, LaporanForm
from .models import Pertanyaan, Jawaban, Laporan
import json

# from chartjs.views.lines import BaseLineChartView

# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/home')
        
    return render(request, 'registration/login.html')
       
def home_kuesioner(request):
    return render(request, 'main/isi-kuesioner/index.html')

def cari_alumni(request):
    return render(request, 'main/cari-alumni.html')

def tentang(request):
    return render(request, 'main/tentang.html')

def kontak(request):
    return render(request, 'main/kontak.html')

""" 
    Ini biar gak pusing pas liat function nya.
    Guna nya sebagai pemisah tiap menu di masing-masing function,
    
    ####################################
    #####       CRUD - Alumni      #####
    ####################################
    
"""

def lihat_alumni(request):
    return render(request, 'backend/alumni/lihat-alumni.html')

""" 
    Ini biar gak pusing pas liat function nya.
    Guna nya sebagai pemisah tiap menu di masing-masing function,
    
    ####################################
    #####     CRUD - Pertanyaan    #####
    ####################################
    
"""

def lihat_pertanyaan(request):
    lihat = Pertanyaan.objects.all()
    
    return render(request, 'backend/pertanyaan/pertanyaan.html', {'lihat': lihat})

def tambah_pertanyaan(request):
    if request.method == 'POST':
        form = PertanyaanForm(request.POST)
        
        if form.is_valid():
            pertanyaan = form.save(commit=False)
            pertanyaan.save()
            
            return redirect('/backend/pertanyaan')
        
    else:
        form = PertanyaanForm()
        
    return render(request, 'backend/pertanyaan/tambah-pertanyaan.html', {'form': form})

def detail_pertanyaan(request, detail_id):
    lihat_detail = get_object_or_404(Pertanyaan, id=detail_id)
    return render(request, 'backend/pertanyaan/detail-pertanyaan.html', {'lihat_detail': lihat_detail})

def update_pertanyaan(request, update_id):
    apdet = Pertanyaan.objects.get(id=update_id)
    
    if request.method == 'POST':
        form = PertanyaanForm(request.POST, instance=apdet)
        
        if form.is_valid():
            form.save()
            
            return redirect('/backend/pertanyaan')
        
    else:
        form = PertanyaanForm()
            
    return render(request, 'backend/pertanyaan/update-pertanyaan.html', {'form': form})

def hapus_pertanyaan(request, delete_id):
    Pertanyaan.objects.filter(id=delete_id).delete()
    
    return redirect('/backend/pertanyaan')

""" 
    Ini biar gak pusing pas liat function nya.
    Guna nya sebagai pemisah tiap menu di masing-masing function,
    
    ####################################
    #####      CRUD - Jawaban      #####
    ####################################
    
"""

def lihat_jawaban(request):
    lihat = Jawaban.objects.all()
    
    return render(request, 'backend/jawaban/jawaban.html', {'lihat': lihat})

def tambah_jawaban(request):
    if request.method == 'POST':
        form = JawabanForm(request.POST)
        
        if form.is_valid():
            jawaban = form.save(commit=False)
            jawaban.save()
            
            return redirect('/backend/jawaban')
        
    else:
        form = JawabanForm()
        
    return render(request, 'backend/jawaban/tambah-jawaban.html', {'form': form})

def update_jawaban(request, update_id):
    apdet = Jawaban.objects.get(id=update_id)
    
    if request.method == 'POST':
        form = JawabanForm(request.POST, instance=apdet)
        
        if form.is_valid():
            form.save()
            
            return redirect('/jawaban')
        
    else:
        form = JawabanForm()
            
    return render(request, 'main/jawaban/update_jawaban.html', {'form': form})


def hapus_jawaban(request, delete_id):
    Jawaban.objects.filter(id=delete_id).delete()
    
    return redirect('/backend/jawaban')

""" 
    Ini biar gak pusing pas liat function nya.
    Guna nya sebagai pemisah tiap menu di masing-masing function,
    
    ####################################
    #####      CRUD - Laporan      #####
    ####################################
    
"""

def lihat_laporan(request):
    lihat = Laporan.objects.all()
    
    return render(request, 'backend/laporan/laporan.html', {'lihat': lihat})
    
def tambah_laporan(request):
    if request.method == 'POST':
        form = LaporanForm(request.POST, request.FILES)
        
        if form.is_valid():
            laporan = form.save(commit=False)
            laporan.save()
            
            return redirect('/backend/laporan')
        
    else:
        form = LaporanForm()
        
    return render(request, 'backend/laporan/tambah-laporan.html', {'form': form})

def detail_laporan(request, detail_id):
    lihat = get_object_or_404(Laporan, id=detail_id)
    return render(request, 'backend/laporan/detail-laporan.html', {'lihat': lihat})

def update_laporan(request, update_id):
    apdet = Laporan.objects.get(pk=update_id)
    
    if request.method == 'POST':
        form = LaporanForm(request.POST or None, request.FILES, instance=apdet)
        
        if form.is_valid():
            form.save()
            
            return redirect('/backend/laporan')
        
    else:
        form = LaporanForm()
            
    return render(request, 'backend/laporan/update-laporan.html', {'form': form, 'apdet': apdet})
    
def hapus_laporan(request, delete_id):
    Laporan.objects.filter(id=delete_id).delete()
    
    return redirect('/backend/laporan')

""" 
    Ini biar gak pusing pas liat function nya.
    Guna nya sebagai pemisah tiap menu di masing-masing function,
    
    ####################################
    #####        Menu Grafik       #####
    ####################################
    
"""
    
def lihat_grafik(request):
    label = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"]
    data = [120, 75, 91, 60, 55, 81, 100, 38]
    
    context = {
        "label": json.dumps(label),
        "data": json.dumps(data),
    }
    
    return render(request, 'backend/grafik/grafik.html', context)
    

