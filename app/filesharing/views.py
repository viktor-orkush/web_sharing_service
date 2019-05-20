from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect

from filesharing.forms import DocumentForm
from filesharing.models import Document


def home(request):
    documents = Document.objects.all()
    return render(request, 'home.html', { 'documents': documents })


def form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'form_upload.html', {
        'form': form
    })