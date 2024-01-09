from flask import Blueprint, jsonify, request

from modules.demanda.dao import DAODemanda
from modules.demanda.modelo import Demanda
from modules.demanda.sql import SQLDemanda

demanda_controller = Blueprint('demanda_controller', __name__)
dao_demanda = DAODemanda()
module_name = 'demanda'

def get_demanda():
    demandas = dao_demanda.get_all()
    results = [demanda.__dict__ for demanda in demandas]
    response = jsonify(results)
    response.status_code = 200
    return response

def get_demanda_by_nome(demanda):
    demandas = dao_demanda.get_by_demanda(demanda)
    results = [demanda.__dict__ for demanda in demandas]
    response = jsonify(results)
    response.status_code = 200
    return response

def delete_demanda_by_nome(demanda):
    dao_demanda.delete_by_demanda(demanda)
    response = jsonify({"message": "Demanda deletada com sucesso!"})
    response.status_code = 200
    return response


def buscar_demanda(demanda = None):

    if demanda:
        return get_demanda_by_nome(demanda)
    return get_demanda()

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

@demanda_controller.route(f'/{module_name}/buscar/', methods = ['GET'])
def get_buscar_demanda():
    demanda = request.args.get('demanda')
    print("buscar demanda:===",demanda)


    results = buscar_demanda(demanda)
    return results

@demanda_controller.route(f'/{module_name}/deletar/', methods = ['DELETE'])
def delete_demanda():
    demanda = request.args.get('demanda')
    print("buscar demanda:===",demanda)
    existe_demande = buscar_demanda(demanda)
    if not existe_demande:
        return "Demanda não encontrada"
    results = delete_demanda_by_nome(demanda)
    return results