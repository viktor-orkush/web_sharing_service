from django.shortcuts import render, redirect
from django.utils.text import get_valid_filename

from app.tasks import delete_file_schedule
from filesharing.forms import DocumentForm
from filesharing.models import Document


def home(request):
    documents = Document.objects.all()
    return render(request, 'home.html', { 'documents': documents })

def form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            new_document = form.save()
            #task schedule to delete file from server
            doc_name = new_document.document.name
            file_live_time = new_document.file_live_time
            delete_file_schedule(doc_name, schedule=file_live_time)
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'form_upload.html', {
        'form': form
    })