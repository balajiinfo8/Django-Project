from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import TODOViews
from rest_framework.routers import DefaultRouter
from .views import TODOViews

router = DefaultRouter()
router.register(r'todo', TODOViews, basename='todo')  # ✅ Registers ViewSet

urlpatterns = [
    path('', include(router.urls)),
]
