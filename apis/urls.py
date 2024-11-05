from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
   path('register/', UserRegistrationView.as_view(), name='register'),
   path('login/', CustomTokenObtainPairView.as_view(), name='login'),
   path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]