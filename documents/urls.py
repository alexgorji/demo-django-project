from django.urls import path

from .views import DocumentCreateView, DocumentListView, DocumentDeleteView, show_document_file

app_name = 'documents'

urlpatterns = [
    path('', DocumentListView.as_view(), name='list-document'),
    path('new', DocumentCreateView.as_view(), name='create-document'),
    path('delete/<int:pk>', DocumentDeleteView.as_view(), name='delete-document'),
    path('<int:pk>', show_document_file, name='show-document')
]
