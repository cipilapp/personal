from dao.grua_dao import GruaDAO
from motor import motor_izaje
from config.config_db import DB_PARAMS

class GruaController:
    def __init__(self):
        self.dao = GruaDAO(DB_PARAMS)

    def recomendar_grua(self, datos_usuario):

        #Traigo los datos de la base de datos
        gruas = self.dao.obtener_gruas()

        # Aquí puedes validar, transformar o enriquecer datos si es necesario
        resultado = motor_izaje(datos_usuario, gruas)
        return resultado