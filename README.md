# Gestor Entregas Comidas Cornershop
Por: Leonardo Patiño

## MANUAL DE INSTALACIÓN

### Características

Características habituales proporcionadas por Django, como la arquitectura MVC, ORM, plantillas, almacenamiento en caché y una interfaz de administración automática.
Y celerys que trabaja con colas de tareas asíncrona para trabajos que se basa en el paso de mensajes distribuidos.

### Pasos

- Clonar repositorio
	```
	git clone https://github.com/leoesleoesleo/backend_test.git
	```
- Crear entorno virtual

    anaconda
	```
	conda create -n gestorComidas python=3.7.9 
    conda activate gestorComidas
	```
	virtualenv
	```
	virtualenv gestorComidas -p python3.7.9
    source gestorComidas/bin/activate
    ```

- Navegar hasta la carpeta del proyecto para instalar dependencias
    ```
    pip install -r requirements.txt
    ```
    
- Migrar la base de datos    
    ```
    python manage.py migrate
    ```
- Cargar datos iniciales
    ```
    python manage.py loaddata gestorComidas/fixtures/posts-data.json
    ```

- Ver tareas con Celery
    ```
    celery -A backend_test worker -l INFO
    ```
    
- Validar cobertura de la aplicación  
    ```
  coverage run -m pytest -v -p no:cacheprovider --junitxml=junit/test-results.xml --cov=. --cov-report=xml --cov-report=html  
    ```    
    
- Iniciar programa
    ```
    python manage.py runserver
    ```
    ```sh
    127.0.0.1:8000
    ```


## MANUAL TÉCNICO

### Contexto

<p align="justify">
  El antiguo proceso consiste en que una persona (Nora) envíe un mensaje de texto vía Whatsapp a todos los empleados chilenos, el mensaje contiene el menú de hoy con las diferentes alternativas para el almuerzo.
</p>

> ¡Hola!
> Comparto con ustedes el menú de hoy :)
>
> Opción 1: Pastel de maíz, Ensalada y Postre
> Opción 2: Arroz, Ensalada y Postre con Nugget de Pollo
> Opción 3: Arroz con Hamburguesa, Ensalada y Postre
> Opción 4: Ensalada y postre de pollo Premium.
>
> ¡Que tengas un buen día!


<p align="center">
  <a href="#"><img src="https://leoesleoesleo.github.io/imagenes/diagrama_contexto.png"></a>
</p>
<br/>
<br/>

## Nuevo Programa

<p align="justify">
 Se construye dos módulos, módulo admin para que el usuario Nora inserte, edite y elimine el menú, Envié los recordatorios por medio de slack, también para que visualice las preferencias de los empleados. 
</p>
<p align="justify">
El módulo de usuario podrá insertar, editar y eliminar las preferencias del menú, también podrá visualizar el menú del día y los recordatorios:

## Diagrama Cero
	
</p>
<p align="center">
  <a href="#"><img src="https://leoesleoesleo.github.io/imagenes/diagrama_cero.png"></a>

## Diagrama BPMN

</p>
<p align="center">
  <a href="#"><img src="https://leoesleoesleo.github.io/imagenes/diagrama_bpmn.png"></a>
</p>

## Caso de Uso

<p align="center">
  <a href="#"><img src="https://leoesleoesleo.github.io/imagenes/caso_de_uso.png"></a>
</p>

## Arquitectura

Requerimientos Funcionales
-	Crea un menú para una fecha específica.
-	Enviar un recordatorio de Slack con el menú de hoy a todos los empleados chilenos
-	Elija su comida preferida (hasta las 11 AM CLT).
-	Especificar personalizaciones (por ejemplo, sin tomates en la ensalada).
-	Nora debería ser el único usuario que pueda ver lo que han solicitado los empleados de Cornershop y crear y editar el menú de hoy.
-	Los empleados deberían poder especificar lo que quieren para el almuerzo, pero no deberían poder ver lo que otros han solicitado.
-	Los recordatorios de holgura deben contener una URL al menú de hoy con el siguiente Patrón https://nora.cornershop.io/menu/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx (un UUID)
-	Esta página no debe requerir la autenticación de ningún amable.

Requerimientos no Funcionales
-	El dominio nora.cornershop.io, se establece la URL como una variable de entorno.
-	Los recordatorios son asíncronos - (Celery)
-	Las pruebas unitarias son escalables – (pytest)
-	La Cobertura del programa llega a un 88% (Coverage)
-	Las Funciones y métodos están comentados
-	El programa proporciona logs de información y errores
-	El programa cuenta con manual de instalación
-	Se implementa el patrón de diseño MVT de Django que incrementa la seguridad de los datos.

## Patrón de diseño MVT

<p align="justify">
Promueve el acoplamiento débil y la estricta separación entre las piezas de la aplicación, es fácil hacer cambios en un lugar particular sin afectar otras piezas de la aplicación. En las funciones de vista, por ejemplo, se separar la lógica de negocios de la lógica de presentación usando un sistema de plantillas. Con la capa de la base de datos, aplicamos esa misma filosofía para el acceso lógico a los datos.
</p>
<p align="center">
  <a href="#"><img src="https://leoesleoesleo.github.io/imagenes/patron_dise%C3%B1o.png"></a>
</p>

## Diagrama E-R

<p align="center">
  <a href="#"><img src="https://leoesleoesleo.github.io/imagenes/diagrama_er.png"></a>
</p>

## Cobertura

<p align="center">
  <a href="#"><img src="https://leoesleoesleo.github.io/imagenes/cobertura.png"></a>
</p>



