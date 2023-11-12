# Ejemplo de login con Flet
# login_flet_python

Este ejemplo muestra cómo crear una web de login con el framework Flet.

## Instalación

Para usar este ejemplo, primero debes instalar el framework Flet:

pip install flet

## Ejecución

A continuación, puedes crear un nuevo archivo `app.py` con el código anterior y ejecutarlo:

python app.py

Esto abrirá una aplicación web en tu navegador. Si no estás autenticado, verás el formulario de login. Si introduce los datos de un usuario existente, se autenticará y se le redirigirá a la página principal.

Descripción del código
El código está dividido en dos partes:

La primera parte crea la aplicación Flet y las rutas.
La segunda parte carga las plantillas y procesa las solicitudes.
Creación de la aplicación Flet y las rutas
La primera parte del código crea una aplicación Flet y las rutas. La aplicación se crea con la función flet.App(). Las rutas se crean con la función flet.route().

En este ejemplo, hay dos rutas:

/: Muestra el formulario de login si el usuario no está autenticado, o redirige a la página principal si lo está.
/login: Procesa el formulario de login y autentica al usuario si los datos son correctos.
Carga de las plantillas y procesamiento de las solicitudes
La segunda parte del código carga las plantillas y procesa las solicitudes. Las plantillas se cargan con la función flet.template(). Las solicitudes se procesan con la función flet.render().

En este ejemplo, hay dos plantillas:

login.html: Muestra el formulario de login.
home.html: Muestra la página principal.
El formulario de login se procesa con la ruta /login. La ruta primero obtiene los datos del formulario con la función request.form. A continuación, valida los datos y comprueba si el usuario existe. Si el usuario existe y la contraseña es correcta, el usuario se autentica y se le redirige a la página principal.

La página principal se muestra con la ruta /. La ruta primero comprueba si el usuario está autenticado. Si lo está, muestra la página principal con los datos del usuario. Si no lo está, redirige al formulario de login.

Extensiones
Este ejemplo es solo un punto de partida. Puedes extenderlo para añadir nuevas funcionalidades, como:

Validación más estricta de los datos del formulario.
Almacenamiento de los datos de los usuarios en una base de datos.
Soporte para usuarios con diferentes roles.
