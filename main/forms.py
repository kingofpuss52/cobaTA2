from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Jawaban, Laporan, Pertanyaan

class CustomUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = "__all__"

class PertanyaanForm(forms.ModelForm):
    class Meta:
        model = Pertanyaan
        fields = "__all__"
        
class JawabanForm(forms.ModelForm):
    class Meta:
        model = Jawaban
        fields = "__all__"
        
class LaporanForm(forms.ModelForm):
    class Meta:
        model = Laporan
        fields = "__all__"