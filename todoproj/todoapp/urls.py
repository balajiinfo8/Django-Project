# from django.urls import path , include
# from .views import todo_view
# from rest_framework.routers import DefaultRouter


# router = DefaultRouter()
# router.register(r'todo/',todo_view,basename='crud')

# urlpatterns = [
#     path('',include(router.urls)),
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import todo_view

router = DefaultRouter()
router.register(r'todo', todo_view, basename='todo')

urlpatterns = [
    path('', include(router.urls)),
]
