from flask import Blueprint, jsonify, request

from modules.demanda.dao import DAODemanda
from modules.demanda.modelo import Demanda
from modules.demanda.sql import SQLDemanda

demanda_controller = Blueprint('demanda_controller', __name__)
dao_demanda = DAODemanda()
module_name = 'demanda'

def get_demanda():
    # if(id):
    #     demandas = dao_demanda.get_by_id()
    #     results = [demanda.__dict__ for demanda in demandas]
    #     response = jsonify(results)
    #     response.status_code = 200
    #     return response

    demandas = dao_demanda.get_all()
    results = [demanda.__dict__ for demanda in demandas]
    response = jsonify(results)
    response.status_code = 200
    return response

def create_demanda():
    demandas = request.json
    erros = []
    for data in demandas:
        for campo in SQLDemanda._CAMPOS_OBRIGATORIOS:
            if campo not in data.keys() or not data.get(campo, '').strip():
                erros.append(f'O campo {campo} é obrigatorio')
        if dao_demanda.get_by_demanda(**data):
            erros.append(f'Já existe uma demanda com esse nome')
        if erros:
            response = jsonify(erros)
            response.status_code = 401
            return response

        demanda = Demanda(**data)
        demanda = dao_demanda.salvar(demanda)
        print(demanda)
    response = jsonify('sucesso')
    response.status_code = 201
    return response



@demanda_controller.route(f'/{module_name}/', methods = ['GET', 'POST'])
def get_or_create_demanda():
    if request.method == 'GET':
        return get_demanda()
    else:
        return create_demanda()

# @demanda_controller.route(f'/{module_name}/<id>', methods = ['GET', 'POST'])
# def get_demanada_by_id(id:int):
#     return get_demanda(id)