import pytest
from gestorComidas.models import Recordatorio
from django import urls
from django.test import Client, TestCase
from faker import Faker
from gestorComidas.tasks import proceso_celery

fake = Faker()


@pytest.mark.django_db
def test_menu_creation():
    record = Recordatorio.objects.create(
        fecha=fake.date(),
        url='www')
    record.save()
    assert record.url == 'www'


@pytest.mark.django_db
def test_render_views_menu(client, menu='arroz', url='www'):
    task = proceso_celery(menu, url)
    assert task == 'envioOK'


class IngresoTest(TestCase):
    def setUp(self):
        self.list_url_admin = urls.reverse('ingresar', args=[1])
        self.list_url_usuario = urls.reverse('ingresar', args=[2])
        self.client = Client()
        self.url = 'https://nora.cornershop.io'

    @pytest.mark.django_db
    def test_ingreso_admin(self):
        session = self.client.session
        session['idUsuario'] = 1
        session['url_slack'] = self.url
        session.save()
        response = self.client.get(self.list_url_admin)
        self.assertEqual(response.status_code, 200)

    @pytest.mark.django_db
    def test_ingreso_usuario(self):
        session = self.client.session
        session['idUsuario'] = 2
        session['url_slack'] = self.url
        session.save()
        response = self.client.get(self.list_url_usuario)
        self.assertEqual(response.status_code, 200)
