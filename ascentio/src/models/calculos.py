from db import db
from datetime import datetime


class CalculadoraModel(db.Model):
    __tablename__ = 'calculadoras'

    id = db.Column(db.Integer, primary_key=True)
    calculo = db.Column(db.String(), nullable=False)   
    resultado = db.Column(db.String(), nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, calculo, resultado):
        self.calculo = calculo
        self.resultado = resultado

    def json(self):
        return {
            'id': self.id,
            'calculo': self.calculo,
            'resultado': self.resultado
        }

    def insert_calculo(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_filtrados(self, filterColumns={}):

        if filterColumns['id'] == '0':
            filter_by = []
        else:
            filter_by = [CalculadoraModel.id == filterColumns['id']]

        persistidos = (
            db.session.query(
                CalculadoraModel
            ).filter(
                *filter_by
            )
        ).order_by(
                CalculadoraModel.id.asc()
            )   

        paginado = persistidos.paginate(1, per_page=100)

        return paginado.items
