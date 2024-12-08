from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Cliente

class ClienteViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.cliente = Cliente.objects.create(
            mes="Enero",
            saldo=100.00,
            dato_usado=50.00,
            minuto_usado=30.00,
        )
        
    
    def test_get_cliente_by_id(self):
        response = self.client.get(f'/telcox_api/cliente/{self.cliente.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["mes"], "Enero")
        self.assertEqual(float(response.data["saldo"]), 100.00)
    def test_get_cliente_not_found(self):
        response = self.client.get('/telcox_api/cliente/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data["error"], "Cliente not found")
    def test_get_all_clientes(self):
        Cliente.objects.create(
            mes="Febrero",
            saldo=200.00,
            dato_usado=100.00,
            minuto_usado=60.00,
        )
        response = self.client.get('/telcox_api/cliente/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Ya había un cliente en setUp

    def test_get_all_clientes_empty(self):
            Cliente.objects.all().delete()  # Elimina todos los clientes
            response = self.client.get('/telcox_api/cliente/')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data, [])
