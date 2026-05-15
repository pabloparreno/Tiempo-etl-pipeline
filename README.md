PRUEBA TÉCNICA ALTEN
La aplicación extrae datos de la API de OpenWeather, transforma los datos y los sube a Big Query. Todo orquestado con AirFlow.

Para Desplegar la aplicación en local y su correcto funcionamiento. Se requiere instalar las dependencias del archivo requirements.txt.
Para ello ejecutar el comando indicado en el Dockerfile

Debemos crear un archivo .env y recrearlo según el archivo .env.example

Se requiere iniciar sesión en https://openweathermap.org/ para generar la Api key necesaria de añadir en el archivo .env 

Es necesario generar el archivo json de de credenciales de google cloud. Dentro de GCP debemos generar una service account y darle los permisos de escritura de Big query. Por último renombrar el archivo como credenciales.json y añadirlo a la carpeta config.

Las credenciales para airflow serán usuario:admin contraseña:admin

Manual de usuario:

Crear .env
copy .env.example .env
docker-compose up --build
Añadir credenciales
config/credenciales.json
Ejecutar
docker-compose up --build
Airflow
http://localhost:8080