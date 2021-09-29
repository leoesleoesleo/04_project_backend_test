import pytest
from gestorComidas.models import Menu
from gestorComidas.formenu import FormMenu
from django import urls
from faker import Faker

fake = Faker()


@pytest.mark.django_db
@pytest.mark.parametrize('param', [
    ('crear_menu')
])
def test_render_views_menu(client, param):
    temp_url = urls.reverse(param)
    resp = client.get(temp_url)
    assert resp.status_code == 200


@pytest.mark.django_db
def test_menu_creation():
    menu = Menu.objects.create(
        menu='arroz',
        fecha=fake.date())
    menu.save()
    assert menu.menu == 'arroz'


@pytest.mark.django_db
def test_menu_creation_count():
    Menu.objects.create(
        menu=fake.name(),
        fecha=fake.date())
    assert Menu.objects.count() == 1


def test_renew_form_date_field_label():
    form_data = {
        'menu' : fake.name(),
        'fecha': fake.date()}
    form = FormMenu(data=form_data)
    assert form.is_valid()
