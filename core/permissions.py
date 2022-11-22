from rest_framework import permissions
from _auth.models import CustomerProfile, ResturantProfile, DriverProfile


def getUsers(request):
    users = {}
    try:
        customer = CustomerProfile.objects.get(user=request.user)
        users['customer'] = customer
    except:
        users['customer'] = None
    try:
        resturant = ResturantProfile.objects.get(user=request.user)
        users['resturant'] = resturant
    except:
        users['resturant'] = None
    try:
        driver = DriverProfile.objects.get(user=request.user)
        users['driver'] = driver
    except:
        users['driver'] = None
    return users

class IsAdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        else:
            return False

class ProductPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        users = getUsers(request)
        if request.method == "GET" and (users['customer'] or users['resturant'] or users['driver']):
            return True
        
        if request.method != "GET" and users['resturant']:
            return True
        else :
            return False 

class MenuPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        users = getUsers(request)
        if request.method == "GET" and (users['customer'] or users['resturant'] or users['driver']):
            return True
        
        if request.method != "GET" and users['resturant']:
            return True
        else :
            return False 

class OrderPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        users = getUsers(request)
        if (request.method == "GET" or request.method == "PUT") and (users['customer'] or users['resturant'] or users['driver']):
            return True
        
        elif users['customer']:
            return True
        
        else:
            return False 