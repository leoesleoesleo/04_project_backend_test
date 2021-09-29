from celery import shared_task
from .models import Recordatorio, Usuario
from datetime import datetime
import uuid


@shared_task
def proceso_celery(menu, url_slack):
	url = f'{url_slack}/{menu}/{str(uuid.uuid4())}'
	fecha = datetime.today().strftime('%Y-%m-%d %H:%M')
	users = Usuario.objects.all()
	for user in users:
		Recordatorio(
			fecha=fecha,
			url=url,
			idUsuario_id=user.idUsuario,).save()
	return 'envioOK'
