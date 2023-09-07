from django.urls import path, include
from . import views

# cloth_patterns = [
#     path("", views.ProductView.get_cloth, name='cloth'),
#     path('<int:product_id>/', views.ProductView.get_cloth_detail, name="cloth-detail")
# ]
# shoes_patterns = [
#     path("", views.ProductView.get_shoes, name='shoes'),
#     path('<int:product_id>/', views.ProductView.get_shoes_detail, name="shoes-detail")
# ]

urlpatterns = [
    path("", views.IndexView.as_view(), name='index'),
    path("<str:category>/", views.ListProduct.as_view(), name='cloth'),
    path('<str:category>/<int:product_id>/', views.DetailProduct.as_view(), name="product-detail")
    # path("cloth/", include(cloth_patterns)),
    # path("shoes/", include(shoes_patterns)),
]


