Descripción del proyecto:

La aplicación extrae datos de la API de OpenWeather, transforma los datos y los sube a Big Query. Todo orquestado con AirFlow de manera local con Docker desktop

Manual de usuario:

Se requiere iniciar sesión en https://openweathermap.org/ para generar la Api key necesaria de añadir en el archivo .env 

Es necesario generar el archivo json de credenciales de google cloud. Para ello Dentro de GCP, en el desplegable de servios, dejamos el cursor en IAM y administración y accedemos a cuentas de servicio. Una vez ahí debemos crear una cuenta de servicio y darle los roles de administrador de Big query y editor de datos de Big query.

Debemos Crear .env a la misma altura que .env.example

En el archivo .env, añadir la Api Key generada anteriormente

Ejecutar el comando: copy .env.example .env

Crear una carpeta config y añadir las credenciales generadas en gcp por la service account. Debe quedar así:
config/credenciales.json

Abrir Docker desktop

Ejecutar
docker-compose up --build
Puede ser que haya que actualizar wsl

Acceder a localhost:
http://localhost:8080
Las credenciales para airflow serán usuario:admin contraseña:admin

Una vez en la interfaz de Airflow, simplemente ejecutar la pipeline y comprobar que los datos se han insertado correctamente.