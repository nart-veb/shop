from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .models import Product, Stock
from django.db.models import Q


class IndexView(View):
    # главная страница
    def get(self, request):
        return render(request, 'shop/index.html')


class ProductView(View):
    # раздел товаров

    # def get_cloth(request):
    #     product_list = Product.objects.filter(~Q(category__title="Обувь"))
    #     context = {
    #         'product_list': product_list,
    #     }
    #     return render(request, 'shop/product/product.html', context)
    #
    # def get_shoes(request):
    #     product_list = Product.objects.filter(category__title="Обувь")
    #     context = {
    #         'product_list': product_list,
    #     }
    #     return render(request, 'shop/product/product.html', context)

    # def get_cloth_detail(request, product_id):
    #     product = get_object_or_404(Product, pk=product_id)
    #     size = Stock.objects.filter(product=product_id, count__gt=0)
    #     return render(request, 'shop/product/product_detail.html', {'product': product, 'size_list': size})
    #
    # def get_shoes_detail(request, product_id):
    #     product = get_object_or_404(Product, pk=product_id)
    #     return render(request, 'shop/product/product_detail.html', {'product': product})
    pass


class ListProduct(ListView):
    template_name = 'shop/product/product.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        return Product.objects.filter(category__title=self.kwargs.get("category"))


class DetailProduct(DetailView):
    model = Product
    template_name = 'shop/product/product_detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'product_id'
