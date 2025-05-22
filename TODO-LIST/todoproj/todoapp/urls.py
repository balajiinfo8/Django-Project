from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TODOViews
from rest_framework.routers import DefaultRouter
from .views import TODOViews

# router = DefaultRouter()
# router.register(r'todo', TODOViews, basename='todo')  # ✅ Registers ViewSet
#
# urlpatterns = [
#     path('', include(router.urls)),
# ]

todolist = TODOViews.as_view({
    'get': 'list',
    'post': 'create',
})

todo_detail = TODOViews.as_view({
    'get': 'list',
    'put': 'update',
    'patch' : 'partial_update',
    'delete': 'destroy',
})

urlpatterns = [
    path('todo/', todolist, name='todo-list'),
    path('todo/<int:pk>/', todo_detail, name='todo-details')
]
