from flask_restplus import Resource, reqparse, fields
from flask import request
import json
from datetime import datetime
from config import config
from models.calculos import CalculadoraModel
from api import api
import math


calculos = api.namespace('Calculos')

calculo_model = api.model('calculo', {
    'calculo': fields.String(description='String para calculo. Solo para persistir.')
})

@calculos.route('')
class Calculos(Resource):

    @calculos.expect(calculo_model)
    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument('calculo')  
        data = parser.parse_args()

        try:
            # operaciones = '3.5 + 4 - log(23.2) ^ (2-1) * -1'
            operaciones = data['calculo']
            operaciones = operaciones.replace('log', 'math.log')
            operaciones = operaciones.replace('^', '**')
            res = str(eval(operaciones))
            
        except:
            ERROR_MESSAGE = config['Messages']['ERROR_MESSAGE']
            ERROR_MESSAGE['error']['code'] = config['ErrorCodes']['NOT_MATCH']
            ERROR_MESSAGE['error']['message'] = config['Messages']['Calculos']['CREATE_CALCULO']
            return ERROR_MESSAGE

        if data['calculo']:
                data['resultado'] = res
                nuevo_calculo = CalculadoraModel(**data)
                respuesta = CalculadoraModel.insert_calculo(nuevo_calculo)
                return {'Resultado': res}
        else:
            ERROR_MESSAGE = config['Messages']['ERROR_MESSAGE']
            ERROR_MESSAGE['error']['code'] = config['ErrorCodes']['DB_ERROR']
            ERROR_MESSAGE['error']['message'] = config['Messages']['Calculos']['PROCESS_CALCULO']
            return ERROR_MESSAGE


    @calculos.doc(params={
        'filterColumns': """\{
            "id":"0"
            \}"""
        })
    def get(self):

        parser = reqparse.RequestParser()
        parser.add_argument('filterColumns', default="{}")
        data = parser.parse_args()

        if(len(data['filterColumns'])>2):
            data['filterColumns'] = json.loads(data['filterColumns'].replace('\'', "\""))  
        else:
            data['filterColumns'] = {'id':'0'}

        try:
            calculos_persistidos = CalculadoraModel.get_filtrados(data['filterColumns'])           

            if not calculos_persistidos:
                ERROR_MESSAGE = config['Messages']['ERROR_MESSAGE']
                ERROR_MESSAGE['error']['code'] = config['ErrorCodes']['NOT_FOUND']
                ERROR_MESSAGE['error']['message'] = config['Messages']['Calculos']['CALCULO_NOT_FOUND']
                return ERROR_MESSAGE

            return {'resutados': [calculos.json() for calculos in calculos_persistidos]}
        
        except:
            ERROR_MESSAGE = config['Messages']['ERROR_MESSAGE']
            ERROR_MESSAGE['error']['code'] = config['ErrorCodes']['DB_ERROR']
            ERROR_MESSAGE['error']['message'] = config['Messages']['Calculos']['GET_CALCULO']
            return ERROR_MESSAGE
