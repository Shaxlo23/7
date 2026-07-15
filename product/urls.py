from django.urls import path
from . import views

urlpatterns = [
    path('product/',views.ProductListAPIView.as_view(),name="product-list"),
    path('product/create/',views.ProductCreateAPIView.as_view(),name="product-create"),
    path('product/<int:pk>/',views.ProductRetrieveAPIView.as_view(),name="product-detail"),
    path('product/update/<int:pk>/',views.ProductUpdateAPIView.as_view(),name="product-update"),
    path('product/delete/<int:pk>/',views.ProductDestroyAPIView.as_view(),name="product-update"),
    path('product/detail-update/<int:pk>/',views.ProductUpdateAPIView.as_view(),name="product-update"),
    path('products/detail-delete/<int:pk>',views.ProductRetrieveDestroyAPIView.as_view(),name="product-detail-delete"),
    path('products/<int:pk>/manage/',views.ProductRetrieveUpdateDestroyAPIView.as_view(),name="product-manage"),
]