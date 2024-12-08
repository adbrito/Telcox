from django.urls import path
from .views import ClienteView

urlpatterns = [
    path('cliente/', ClienteView.as_view()),
    path('cliente/<int:cliente_id>/', ClienteView.as_view()),
]
