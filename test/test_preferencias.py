import pytest
from django import urls
from gestorComidas.models import Preferencias
from gestorComidas.formprefer import FormPrefer
from faker import Faker
from django.test import Client, TestCase

fake = Faker()


@pytest.fixture
def create_preferencia():
    return Preferencias


@pytest.mark.django_db
def test_create_preferencia(create_preferencia):
    assert create_preferencia.preferencia


@pytest.mark.django_db
def test_prefer_creation():
    prefer = Preferencias.objects.create(
        preferencia='pollo',
        fecha=fake.date(),
        personaliza=fake.name())
    prefer.save()
    assert prefer.preferencia == 'pollo'


@pytest.mark.django_db
def test_prefer_creation_count():
    Preferencias.objects.create(
        preferencia=fake.name(),
        fecha=fake.date(),
        personaliza=fake.name())
    assert Preferencias.objects.count() == 1


def test_form_prefer():
    form_data = {
        'preferencia' : fake.name(),
        'fecha': fake.date(),
        'personaliza': fake.name()}
    form = FormPrefer(data=form_data)
    assert form.is_valid()


class CrearpreferTest(TestCase):
    def setUp(self):
        self.list_url = urls.reverse('crear_prefer')
        self.client = Client()

    @pytest.mark.django_db
    def test_prefer_post(self):
        session = self.client.session
        session['idUsuario'] = 1
        session.save()
        response = self.client.post(self.list_url, {
            'preferencia' : fake.name(),
            'personaliza' : fake.name(),
            'fecha' : fake.date(),
            'idUsuario' : 1
        })
        self.assertEqual(response.status_code, 200)

    @pytest.mark.django_db
    def test_prefer_get(self):
        session = self.client.session
        session['idUsuario'] = 2
        session.save()
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
