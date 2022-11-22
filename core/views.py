from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_condition import Or
from .models import Product, Menu, Order
from _auth.models import ResturantProfile, CustomerProfile, DriverProfile
from .serializers import ProductSerilaizer, MenuSerilaizer, OrderSerilaizer
from .permissions import ProductPermissions, MenuPermissions, OrderPermissions, IsAdminPermission

class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerilaizer
    permission_classes = (Or(ProductPermissions, IsAdminPermission),)
    def get_queryset(self):
        try:
            resturant = ResturantProfile.objects.get(user=self.request.user)
        except:
            resturant = None
        if resturant:
            products = super().get_queryset().filter(menu_products__resturant=resturant)
            return products
        return super().get_queryset()


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerilaizer
    permission_classes = (Or(ProductPermissions, IsAdminPermission),)
    def get_queryset(self):
        try:
            resturant = ResturantProfile.objects.get(user=self.request.user)
        except:
            resturant = None
        if resturant:
            products = super().get_queryset().filter(menu_products__resturant=resturant)
            return products
        return super().get_queryset()




class MenuListView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerilaizer
    permission_classes = (Or(MenuPermissions, IsAdminPermission),)
    def get_queryset(self):
        try:
            resturant = ResturantProfile.objects.get(user=self.request.user)
        except:
            resturant = None
        if resturant:
            menus = super().get_queryset().filter(resturant=resturant)
            return menus
        return super().get_queryset()


class MenuDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerilaizer
    permission_classes = (Or(MenuPermissions, IsAdminPermission),)
    def get_queryset(self):
        try:
            resturant = ResturantProfile.objects.get(user=self.request.user)
        except:
            resturant = None
        if resturant:
            menus = super().get_queryset().filter(resturant=resturant)
            return menus
        return super().get_queryset()


class OrderListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerilaizer
    permission_classes = (Or(OrderPermissions, IsAdminPermission),)

    def get_queryset(self):
        try:
            resturant = ResturantProfile.objects.get(user=self.request.user)
        except:
            resturant = None
        try:
            driver = DriverProfile.objects.get(user=self.request.user)
        except:
            driver = None
        
        if resturant:
            orders = super().get_queryset().filter(resturant=resturant)
            return orders
        
        if driver:
            orders = super().get_queryset().filter(status="WITHDRIVER")
            return orders
        return super().get_queryset()

    def create(self, request, *args, **kwargs):
        customer = CustomerProfile.objects.get(user=self.request.user)
        resturant = ResturantProfile.objects.get(id=self.request.data["resturant"])
        products = self.request.data["products"]
        products_instance = Product.objects.filter(id__in=products)
        order = Order.objects.create(
            name = self.request.data["name"],
            ordered_by = customer,
            resturant = resturant,

        )
        order.products.set(products_instance)
        serializer = OrderSerilaizer(order)
        return Response(serializer.data) 
    

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerilaizer
    permission_classes = (Or(OrderPermissions, IsAdminPermission),)

    def get_queryset(self):
        try:
            resturant = ResturantProfile.objects.get(user=self.request.user)
        except:
            resturant = None
        if resturant:
            orders = super().get_queryset().filter(resturant=resturant)
            return orders
        return super().get_queryset()

class OrderCancelView(APIView):

    def post(self, request, pk):
        try:
            customer = CustomerProfile.objects.get(user=self.request.user)
        except:
            return Response({
                'success': False,
                'data': None,
                'message': "Only Customers can cancel orders"
            })
        order = Order.objects.get(pk=pk)
        if order.ordered_by == customer and order.status != "CANCELED":
            order.status = "CANCELED"
            order.save()
            return Response({
                'success': True,
                'data': None,
                'message': 'Order canceled successfully'
            })
        else:
            return Response({
                'success': False,
                'data': None,
                'message': "you don't have permission to cancel this order OR order already canceled"
            })

class OrderChangeStatusView(APIView):
    def post(self, request, pk):
        try:
            driver = DriverProfile.objects.get(user=self.request.user)
        except:
            return Response({
                'success': False,
                'data': None,
                'message': "Only Driver can change order status"
            })
        order = Order.objects.get(pk=pk)
        if order.status == "WITHDRIVER":
            order.status = "DELIVERED"
            order.save()
            return Response({
                'success': True,
                'data': None,
                'message': 'Order change status to delivered successfully'
            })
        else:
            return Response({
                'success': False,
                'data': None,
                'message': "order status not changed"
            })
    

