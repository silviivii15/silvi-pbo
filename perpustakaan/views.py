from django.shortcuts import render, redirect
from perpustakaan.models import peminjam

def peminjam(request):
    datas = peminjam.objek.all()

    konteks = {
        'datas' : datas,
    }
    return render(request, 'peminjam.html', konteks)

def nama_buku(request):
    if request.POST:
        form = nama_buku(request.POST)
        if form.is_valid():
            form.save()
            form = nama_buku()

            konteks = {
                'form' : form,
            }
            return render(request, 'nama_buku.html', konteks)

    else:
        form = nama_buku()

        konteks = {
            'form' : form,
        }

        return render(request, 'nama_buku.html', konteks)


