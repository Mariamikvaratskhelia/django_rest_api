from django.urls import path
from .views import item_list_create, item_delete

urlpatterns = [
    path('items/', item_list_create),
    path('items/<int:id>/', item_delete),
]
