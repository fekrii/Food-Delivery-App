from django.urls import path
from core.views import (
    ProductListView, 
    ProductDetailView, 
    MenuListView, 
    MenuDetailView,
    OrderListView,
    OrderDetailView,
    OrderCancelView,
    OrderChangeStatusView
)



urlpatterns = [
    path('products/', ProductListView.as_view()),
    path('products/<int:pk>', ProductDetailView.as_view()),

    path('menu/', MenuListView.as_view()),
    path('menu/<int:pk>', MenuDetailView.as_view()),

    path('order/', OrderListView.as_view()),
    path('order/<int:pk>', OrderDetailView.as_view()),
    path('order/<int:pk>/cancel/', OrderCancelView.as_view()),
    path('order/<int:pk>/change_status/', OrderChangeStatusView.as_view())

]