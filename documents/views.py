import re
from pathlib import Path

from django.forms import ClearableFileInput
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.views.static import serve

from documents.models import Document


class DocumentCreateView(generic.CreateView):
    # form_class = DocumentForm
    model = Document
    fields = ('file',)

    def get_success_url(self):
        return reverse_lazy('documents:list-document')

    def post(self, request, *args, **kwargs):
        files = request.FILES.getlist('file')
        for index, file in enumerate(files[:-1]):
            Document.objects.create(file=file)
        if 'document-create-save' in request.POST:
            return super().post(request, *args, **kwargs)
        else:
            raise ValueError()

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form'].fields['file'].widget = ClearableFileInput(attrs={'multiple': True})
    #     context['document'] = None
    #     return context


class DocumentListView(generic.ListView):
    model = Document


def remove_file_and_parent_if_empty(path):
    if isinstance(path, str):
        path = Path(path)
    parent = path.parent
    try:
        Path.rmdir(path)
        remove_file_and_parent_if_empty(parent)
    except NotADirectoryError:
        Path.unlink(path)
        remove_file_and_parent_if_empty(parent)
    except OSError:
        pass


class DocumentDeleteView(generic.DeleteView):
    model = Document

    def get_success_url(self):
        return reverse_lazy('documents:list-document')

    def dispatch(self, request, *args, **kwargs):
        print('Removing file', self.get_object().file.path)
        remove_file_and_parent_if_empty(self.get_object().file.path)
        return super().dispatch(request, *args, **kwargs)


def show_document_file(request, pk):
    document = get_object_or_404(Document, pk=pk)
    request_url = request.build_absolute_uri()
    domain = re.search(r"//(.*?)/", request_url).group(1)
    if domain.startswith('localhost') or domain.startswith('127.0.0.1'):
        return serve(request, path=document.file.url, document_root='')
    else:
        response = HttpResponse(status=200)
        response['Content-Type'] = ''
        response['X-Accel-Redirect'] = f"{document.file.url}"
    return response
