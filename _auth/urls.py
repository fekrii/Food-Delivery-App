
from django.urls import path

from _auth.serializers import MyTokenObtainPairView
from _auth.views import register_user, ProfileViewSet

app_name = "_auth"

get_profile = ProfileViewSet.as_view({"get": "get_profile"})
urlpatterns = [
    path('register/', register_user),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('profile/my', get_profile),
]
