from django.urls import reverse_lazy
from rest_framework.test import APITestCase
from .models import Personnage

class PersonnageTests(APITestCase):

    def test_list(self):
        url = reverse_lazy('')
        Personnage.objects.create(nom='Test')

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        excepted = [
            {
                'nom': 'Test'            
            }
        ]
        self.assertEqual(excepted, response.json())

    def test_create(self):
        url = reverse_lazy('')

        response = self.client.post(url, data={'nom': 'Test'})
        self.assertEqual(response.status_code, 201)
        excepted = {
            'nom': 'Test'            
        }
        self.assertEqual(excepted, response.json())
    
    def test_update(self):
        personnage = Personnage.objects.create(nom='Test')
        url = reverse_lazy('details', kwargs={'id': personnage.id})

        response = self.client.put(url, data={'nom': 'Retest'})
        self.assertEqual(response.status_code, 200)
        personnage_update = Personnage.objects.get(id=1)
        self.assertEqual(personnage_update.nom, 'Retest')

    def test_delete(self):
        personnage = Personnage.objects.create(nom='Test')
        url = reverse_lazy('details', kwargs={'id': personnage.id})

        response = self.client.delete(url)
        self.assertEqual(response.status_code, 200)