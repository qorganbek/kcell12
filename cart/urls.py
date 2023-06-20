from typing import List

from django.urls import (path, URLPattern, include)
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from . import views
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import routers
from. import views
#
# r = routers.DefaultRouter()
# r.register(r'products', views.ProductModelViewSet)


urlpatterns: List[URLPattern] = [
    path(route='', view=views.CartView.as_view(), name='summary'),
    path(route='payment/', view=views.PaymentView.as_view(), name='payment'),
    path(route='checkout/', view=views.CheckoutView.as_view(), name='checkout'),
    path(route='thank-you/', view=views.ThankYouView.as_view(), name='thank-you'),
    path(route='shop/', view=views.ProductListView.as_view(), name='product-list'),
    path(route='orders/<pk>/', view=views.OrderDetailView.as_view(), name='order-detail'),
    path(route='webhooks/stripe/', view=views.stripe_webhook_view, name='stripe-webhook'),
    path(route='shop/<slug>/', view=views.ProductDetailView.as_view(), name='product-detail'),
    path(route='confirm-order/', view=views.ConfirmOrderView.as_view(), name='confirm-order'),
    path(route='payment/stripe/', view=views.StripePaymentView.as_view(), name='payment-stripe'),
    path(
        route='increase-quantity/<pk>/',
        view=views.IncreaseQuantityView.as_view(),
        name='increase-quantity',
    ),
    path(
        route='decrease-quantity/<pk>/',
        view=views.DecreaseQuantityView.as_view(),
        name='decrease-quantity',
    ),
    path(
        route='remove-from-cart/<pk>/',
        view=views.RemoveFromCartView.as_view(),
        name='remove-from-cart',
    ),
    path('results/', views.SearchView.as_view(), name='search'),
    path('fresults/', views.FilterView.as_view(), name='filter'),
    # path(
    #     route='product/search/',
    #     view=views.RemoveFromCartView.as_view(),
    #     name='',
    # ),
    # path(
    #     route='products/',
    #     view=views.
    # )
]

# urlpatterns += r.urls

app_name: str = 'cart'

# path('product/search/', views.product_search, name='product_search'),
# path('products/?title', views.search_product_by_title),
# path('products/page/<int:page_number>/', views.products, name='products_paginated'),
# path('products/<int:min_price>/<int:max_price>/', product_list, name='product_list_filtered'),
# path(
#     route='products/',
#     view='dima',
#     name='product-search'
# ),


__all__ = ('app_name', 'urlpatterns',)
