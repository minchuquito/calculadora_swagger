config = {
  "AppSettings": {
    "version": "1.0.0",
    'title': 'Ascentio Prueba.',
    'description': 'Swagger calculadora.'
  },
  "Postgres":{
      "username": "postgres",
      "password": "65008",
      "url": "localhost",
      "db": "ascentio",
      "port": "5432"
  },
  # "Postgres":{
  #     "username": "yfhfzubxizedsd",
  #     "password": "f8db3d4f1a2b5d65fe5e11cda6433ee68c851c61692b699dcfae44c6c803b8d4",
  #     "url": "ec2-18-233-83-165.compute-1.amazonaws.com",
  #     "db": "d2b9j2rq0hfj23",
  #     "port": "5432"
  # },
  "port": 5005,
  "host": "0.0.0.0",
  "ErrorCodes": {
    "DB_ERROR": 1,
    "NOT_FOUND": 2,
    "NOT_MATCH": 3
  },
  "Messages": {
    "ERROR_MESSAGE": {
      "error": {
        "code": 0,
        "message": ""
        }
    },
    "Calculos": {
      "PROCESS_CALCULO": "Hubo un problema la persistir el string de calculo.",
      "CREATE_CALCULO": "Hubo un problema en con el string de calculo.",
      "CALCULO_NOT_FOUND": "El calculo especificado no se encontró.",
      "GET_CALCULO": "Hubo un problema al intentar obtener el cálculo."
    }
  }
}
