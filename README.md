# Elecciones 2023

## Enunciado

- En el archivo de `models.py` vas a encontrarte con dos modelos: **PoliticalParties** y **Voters**
- En el archivo de `utils.py` vas a encontrarte dos funciones:
  - **has_voted**
  - **has_voted_percentage**
- Contexto:
  - Este sistema contempla la votaciones para **balotaje**
  - El sitio de ejemplo de votaciones generales: https://resultados.gob.ar/elecciones/1/0/1/-1/-1#agrupaciones
  - Reglas que podrias tener que utilizar: https://www.argentina.gob.ar/dine/clases-de-votos
- Requisitos:
  - Pagina para votación
    - Se ingresa el documento y en segun si ya voto o no:
      - si no voto, puede votar las opciones posibles
      - si ya voto, no puede votar
  - Pagina adminsitracion (con permiso) para realizar el cierre de la votación
    - Boton de cierre
    - Confirmacion
    - Muestra de resultados y ganador
  - Pagina de resultados (publica)
    - en caso de no estar cerrada la votación, muestra el % de votantes que ya votaron y el total de votantes
    - en caso de ya cerrada la votación, muestra los resultados y ganador
  - **Se espera poder tener la información suficiente para en caso de necesitarse se pueda obtener el % de votos a favor de cada partido en determinada zona**

## Requisitos previos

### Docker

Tener instalado docker y docker-compose ver: [documentación oficial](https://www.digitalocean.com/community/tutorials/como-instalar-docker-compose-en-ubuntu-18-04-es)

### Resumen

- Para configurar localmente el proyecto, utilizamos Docker (aunque podes no usarlo).

- Hay un **docker-compose.yml** que tiene, la base de datos (postgres).

- En la configuración local con Docker, se disponibiliza la BD.

- Siguiendo los pasos que se listan a continuación, tendremos disponibles los siguientes contenedores:
  - **DB**: Instancia de BD principal.

## Entorno de desarrollo

Configurar variables de entorno _(modificar los valores si es necesario)._

```bash
cp .env.dist .env
```

Crear el entorno virtual e instalar dependencias:

### Prerequisito

- Tener instalado las librerias de postgres y la base de datos corriendo (ya sea en el entorno de docker-compose o local)

#### Ubuntu

```bash
sudo apt install libpq-dev
```

#### Manjaro

```bash
sudo pacman -S postgresql-libs
```

#### Instalar dependencias de python

```bash
poetry install
```

#### Iniciar el entorno virtual

```bash
poetry shell
```

#### Levantar contenedores

```bash
docker-compose up -d
```

#### Migrations

```bash
cd src

python manage.py migrate
```

#### Carga de datos inicial

```bash
python manage.py load_test_data
```

#### Crear un superuser

```bash
python manage.py createsuperuser
```

#### Iniciar servidor

```bash
python manage.py runserver
```

## Entorno de proyecto

### Herramientas utilizadas

- blue
- flake8
- pre-commit
- pytest
