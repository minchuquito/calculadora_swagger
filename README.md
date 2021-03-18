# calculadora_swagger

Calculadora API con Python y Swagger

  Se utilizó:

1)  Python 3.6
2)  Flask
3)  Base de datos Postgres, va a ser necesario crearla en local.(Nombre ascentio o bien modificar el el config.py)
4)  Será necesario crear un entorno virtual (pipenv) y correr la lista de requerimientos
5)  # cd ~/src
6)  # pipenv shell
7)  # pip install -r requeriments.txt
8)  # pipenv run python app.py
9)  Se configuro para correr en la siguiente url : http://0.0.0.0:5005/
10)  Se utilizó Swagger para probar los metodos POST y GET necesarios para el escenario.

![image](https://user-images.githubusercontent.com/6844399/111676990-82734480-87fd-11eb-8158-22fcaf99db68.png)

Post:
Payload:{"calculo": "string_con_calculo"}, retorna el resultado de ser correcta la expresion.

Get: (se utiliza filterColumns por URL)
  1 - vacio, trae todos los string persistidos con su resultado, string de calculo e Id para identificarlo.
  2 - {"id": "#"} trae un string de calculo ya persistido en base o bien un mensaje de no existe.


Datos de acceso a Postgres:
  Será necesario actualizar los datos de conexion en el siguiente archivo para una prueba local: ~/src/config.py
    "Postgres":{
      "username": "postgres",
      "password": "password",
      "url": "localhost",
      "db": "ascentio",
      "port": "5432"
  }
