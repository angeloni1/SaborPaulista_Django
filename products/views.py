from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from home.models import Products, Categorias, Tabelanutricionals, ProdutoFotos, OndeComprar

# Create your views here.

class ProductsView(View):
    def get(self, request):
        produtos = Products.objects.all()
        categorias = Categorias.objects.all()
        onde_comprar = OndeComprar.objects.all()
        onde_comprar_uf = OndeComprar.objects.values('estado')
        # produtos_dict = {'produtos': produtos  }
        return render(request, "products/products.html", {'produtos': produtos, 'categorias': categorias, 'onde_comprar': onde_comprar, 'uf': onde_comprar_uf})

class ProductsDetailView(View):
    def get(self, request, pk):
        tabela_info = ''
        produto_info = get_object_or_404(Products, pk=pk)
        if produto_info.idnutricional is not None:
            tabela_info = get_object_or_404(Tabelanutricionals, pk= produto_info.idnutricional.id)
        fotos = ProdutoFotos.objects.filter(produtoid=produto_info.id)
        return render(request, "products/product-detail.html", {"produto" : produto_info, "tabela" : tabela_info, "fotos" : fotos})