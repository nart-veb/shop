from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .models import Product, Stock,CardItem, Basket
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse



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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        size_list = Stock.objects.filter(product=self.kwargs.get("product_id"), count__gt=0)
        context['size_list'] = size_list
        return context


class BasketView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'

    def get(self, request):
        basket = Basket.objects.get(user=self.request.user)
        card_item = CardItem.objects.filter(basket=basket)
        # return HttpResponse(f'Thank you {self.request.user.id} {card_item}')
        return render(request, 'shop/basket.html', {'card_item_list': card_item})


class ProductSave(LoginRequiredMixin, View):
    login_url = '/accounts/login/'

    def get(self, request):
        if request.method == 'POST':
            form = Product(request.POST)
            if form.is_valid():
                return HttpResponse('0')
            else:
                return HttpResponse('1')
        else:
            return HttpResponse('2')



