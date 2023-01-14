from django.forms import ModelForm
from django import forms
from perpustakaan.models import Peminjam

class FormData(ModelForm):
  class Meta:
    model = Peminjam
    fields = '__all__'

    widgets = {
      'nis' : forms.TextInput({'class':'form-control'}),
      'nama' : forms.TextInput({'class':'form-control'}),
      'kelas' : forms.TextInput({'class':'form-control'}),
      'keterangan_id' : forms.Select({'class':'form-control'}),

    }