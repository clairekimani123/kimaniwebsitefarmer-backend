
from django.urls import path, include
from .views import (
    AnimalListCreateView, AnimalDetailView, CartAddView, CartListView,
    CartUpdateView, CartRemoveView, CartCheckoutView, OrderListView,
    OrderConfirmView, OrderRejectView
)

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('animals/', AnimalListCreateView.as_view(), name='animal-list-create'),
    path('animals/<int:pk>/', AnimalDetailView.as_view(), name='animal-detail'),
    path('cart/add/', CartAddView.as_view(), name='cart-add'),
    path('cart/', CartListView.as_view(), name='cart-list'),
    path('cart/<int:pk>/update/', CartUpdateView.as_view(), name='cart-update'),
    path('cart/<int:pk>/remove/', CartRemoveView.as_view(), name='cart-remove'),
    path('cart/checkout/', CartCheckoutView.as_view(), name='cart-checkout'),
    path('orders/list/', OrderListView.as_view(), name='order-list'),
    path('orders/<int:pk>/confirm/', OrderConfirmView.as_view(), name='order-confirm'),
    path('orders/<int:pk>/reject/', OrderRejectView.as_view(), name='order-reject'),
]