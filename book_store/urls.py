from django.urls import path
from book_store.views.book_views import BookListCreateAPIView, BookDetail
from book_store.views.cart_views import CartListShopView, CartItemCreateView, CartItemDeleteView
from book_store.views.order_views import OrderHistoryList, PlaceOrderView

urlpatterns = [
    path('books/', BookListCreateAPIView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('cart/', CartListShopView.as_view(), name='cart-detail'),
    path('cart/item', CartItemCreateView.as_view(), name='cart-item-create'),
    path('cart/<int:pk>/', CartItemDeleteView.as_view(), name='cart-item-delete'),

    # path('carts/', views.ShoppingCartList.as_view(), name='cart-list'),
    # path('carts/add/', views.AddToShoppingCart.as_view(), name='add-to-cart'),
    # path('carts/remove/<int:pk>/', views.RemoveFromShoppingCart.as_view(), name='remove-from-cart'),
    path('orders/', OrderHistoryList.as_view(), name='order-history'),
    path('orders/place', PlaceOrderView.as_view(), name='place-order'),
]

