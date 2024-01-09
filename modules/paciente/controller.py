from flask import Blueprint, jsonify, request

from modules.comuns.controller import ControllerComuns
from modules.paciente.dao import DAOPaciente
from modules.paciente.modelo import Paciente
from modules.paciente.sql import SQLPaciente
from modules.sus.controller import ControllerSus

paciente_controller = Blueprint('paciente_controller', __name__)
dao_paciente = DAOPaciente()
sus_controller = ControllerSus()
comuns_controller = ControllerComuns()
module_name = 'paciente'

def create_paciente():
    pacientes = request.json
    erros = []
    for data in pacientes:
        for campo in SQLPaciente._CAMPOS_OBRIGATORIOS:
            if campo not in data.keys() or not data.get(campo, '').strip():
                erros.append(f'O campo {campo} é obrigatorio')
        print('verificando se o cpf existe')
        if dao_paciente.get_by_cpf(data.get('cpf')):
            erros.append(f'já tem cadastro')
        if erros:
            response = jsonify(erros)
            response.status_code = 401
            print(response)
            return response
        if not 'sus' in data:
            paciente = Paciente(**data)
            paciente = dao_paciente.salvar(paciente)
        else:
            paciente_dados = {chave: valor for chave, valor in data.items() if chave != 'sus'}
            paciente = Paciente(**paciente_dados)
            paciente = dao_paciente.salvar(paciente)
            print('pegando cpf para pegar o id do paciente para adicionar o sus ao hitorico')
            print('cpf informado: ', paciente.cpf)
            paciente_id = comuns_controller.get_id_paciente_by_cpf(paciente.cpf)
            print('id do paciente: ',paciente_id)
        print(paciente)
    response = jsonify('sucesso')
    response.status_code = 201
    return response

def get_paciente():
    pacientes = dao_paciente.get_all()
    results = [paciente.__dict__ for paciente in pacientes]
    response = jsonify(results)
    response.status_code = 200
    return response

def get_paciente_by_nome(nome):
    pacientes = dao_paciente.get_by_nome(nome)
    if pacientes:
        results = [paciente.__dict__ for paciente in pacientes]
        response = jsonify(results)
        response.status_code = 200
        return response
    else:
        response = jsonify('nenhum resultado encontrado')
        response.status_code = 404
        return response

def get_paciente_by_mae(mae):
    pacientes = dao_paciente.get_by_mae(mae)
    if pacientes:
        results = [paciente.__dict__ for paciente in pacientes]
        response = jsonify(results)
        response.status_code = 200
        return response
    else:
        response = jsonify('nenhum resultado encontrado')
        response.status_code = 404
        return response

def get_paciente_by_cpf(cpf):
    pacientes = dao_paciente.get_by_cpf(cpf)
    if pacientes:
        results = [paciente.__dict__ for paciente in pacientes]
        response = jsonify(results)
        response.status_code = 200
        return response
    else:
        response = jsonify('nenhum resultado encontrado')
        response.status_code = 404
        return response

def get_paciente_by_data_nasc(data_nasc):
    pacientes = dao_paciente.get_by_data_nasc(data_nasc)
    if pacientes:
        results = [paciente.__dict__ for paciente in pacientes]
        response = jsonify(results)
        response.status_code = 200
        return response
    else:
        response = jsonify('nenhum resultado encontrado')
        response.status_code = 404
        return response

# def get_paciente_by_sus(sus):
#     pacientes = sus_controller.get_by_sus(sus)
#     results = [paciente.__dict__ for paciente in pacientes]
#     response = jsonify(results)
#     response.status_code = 200
#     return response

# def criar_atualizar_paciente():
#     pacientes = request.json
#     if 'sus' in pacientes:
#         paciente_info = {k: v for k, v in pacientes.items() if k!='sus'}
#         paciente = buscar_paciente(paciente_info.get('cpf'))
#         paciente_id = paciente[0]
#         print(paciente_id)
#         if not paciente:
#             paciente = create_paciente(paciente_info)
#             paciente_id = paciente
#
def buscar_paciente(nome = None, mae = None, sus = None, data_nasc = None, cpf = None):

    if nome:
        return get_paciente_by_nome(nome)
    if mae:
        return get_paciente_by_mae(mae)
    if cpf:
        return get_paciente_by_cpf(cpf)
    if data_nasc:
        return get_paciente_by_data_nasc(data_nasc)
    if sus:
        return get_paciente_by_sus(sus)
    return get_paciente()
@paciente_controller.route(f'/{module_name}/', methods = ['GET', 'POST'])
def get_or_create_paciente():
    if request.method == 'GET':
        return get_paciente()
    else:
        print("criar paciente")
        return create_paciente()

# # def get_or_create_sus():
# #    print("pegando sus sus")
# #    if request.method == 'GET':
# #        pass
# #    else:
# #        print("adicionando sus")
# #        return sus_controller.create_sus()
#
@paciente_controller.route(f'/{module_name}/buscar/', methods = ['GET'])
def get_buscar_paciente():
    nome = request.args.get('nome')
    mae = request.args.get('mae')
    sus = request.args.get('sus')
    data_nasc = request.args.get('data_nasc')
    cpf = request.args.get('cpf')

    #cria um dicionario
    params = {'nome':nome, 'mae':mae, 'sus':sus, 'data_nasc':data_nasc, 'cpf':cpf}
    params = {chave: valor for chave, valor in params.items() if valor is not None}
    print('parametros de busca: ', params)

    results = buscar_paciente(**params)
    return results
#
# @paciente_controller.route(f'/{module_name}/pegar/', methods = ['GET'])
# def get_id_paciente_por_cpf():
#     cpf = request.args.get('cpf')
#     print('cpf= ', cpf)
#     id = get_id_by_cpf(cpf)
#     if id is not None:
#         response = jsonify(f'paciente encontrado id : {id}')
#         response.status_code=200