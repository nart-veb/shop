from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name='index'),
    path("<str:category>/", views.ListProduct.as_view(), name='cloth'),
    path('<str:category>/<int:product_id>/', views.DetailProduct.as_view(), name="product-detail"),
    path('accounts/basket/', views.BasketView.as_view(), name='basket'),
    path('product-save/', views.ProductSave.as_view(), name="product-save"),

]


