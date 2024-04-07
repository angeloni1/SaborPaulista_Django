from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from home.models import Documents, Categoriasdocumentos

# Create your views here.

class DocumentosView(View):
    def get(self, request):
        documentos = Documents.objects.all()
        categorias = Categoriasdocumentos.objects.all()
        return render(request, "documentos/documentos.html", {"documentos" : documentos, "categorias" : categorias})

class DocumentoView(View):
    def get(self, request, pk):
        documento = get_object_or_404(Documents, pk=pk)
        return render(request, "documentos/documento.html", {"doc" : documento})
