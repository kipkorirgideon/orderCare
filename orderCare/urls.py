from django.urls import path, include
from rest_framework.routers import DefaultRouter
from orderCare import views
from orderCare import viewsets

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'orders', viewsets.OrderViewSet, basename='order')
router.register(r'customers', viewsets.CustomerViewSet, basename='customer')
router.register(r'items', viewsets.ItemViewSet, basename='item')


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('auth-login/', views.UserLoginView.as_view()),
    path('auth-register/', views.UserRegistrationView.as_view()),
] + router.urls
