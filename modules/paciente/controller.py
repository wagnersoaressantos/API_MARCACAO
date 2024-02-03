from flask import Blueprint, jsonify, request

from modules.comuns.controller import ControllerComuns
from modules.paciente.dao import DAOPaciente
from modules.paciente.modelo import Paciente
from modules.paciente.sql import SQLPaciente
from modules.sus.controller import ControllerSus
from modules.sus.modelo import Sus

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
            paciente_id = comuns_controller.get_id_paciente_by_cpf(paciente.cpf)
            print('id do paciente: ',paciente_id)
            print('sus informado: ', data.get('sus'))
            sus_novo = data.get('sus')
            print(f'solicitando adição do sus: {sus_novo} ao historico do sus')
            params = {'sus': sus_novo, 'paciente_id': paciente_id }
            print('params: ', params)
            dados_sus = sus_controller.pegar_dados()
            print('dados adicionados: ', dados_sus)
        print(paciente)
    response = jsonify('sucesso')
    response.status_code = 201
    return response

def atualizar_paciente():
    pacientes = request.json
    for data in pacientes:
        if'cpf' in data:
            if data.get('cpf')!="":
                id = comuns_controller.get_id_paciente_by_cpf(data.get('cpf'))
                paciente_novo = Paciente(data.get('nome'), data.get('mae'), data.get('data_nasc'), data.get('pai'), id)
                if not 'sus' in data:
                    dao_paciente.atualizar(paciente_novo)
                else:
                    dao_paciente.atualizar(paciente_novo)
                    dados_sus = sus_controller.pegar_dados()
                    paciente_novo.adiciona_sus_no_historico(dados_sus)
            else:
                response = jsonify("Informe o CPF")
                return response
        else:
            response = jsonify("Informe o CPF para relizar a atualização")
            return response
    response = jsonify("sucesso na atualização")
    return response

def delete_paciente(cpf):
    id = comuns_controller.get_id_paciente_by_cpf(cpf)
    if not id:
        response = jsonify({"message":"Paciente não encontrado!"})
        response.status_code = 404
        return response
    dao_paciente.delete_paciente_by_id(id)
    response = jsonify({"message": "Paciente deletado com sucesso!"})
    response.status_code = 200
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

def get_paciente_by_sus(sus):
    paciente_id = sus_controller.get_paciente_by_sus(sus)
    resultado_paciente = dao_paciente.get_by_id(paciente_id)
    list_sus = sus_controller.get_sus_by_paciente_id(paciente_id)
    if list_sus:
        for sus in list_sus:
            resultado_paciente.adiciona_sus_no_historico(sus)
    if resultado_paciente:
        result = resultado_paciente.__dict__
        response = jsonify(result)
        response.status_code = 200
        return response
    else:
        response = jsonify('nenhum resultado encontrado')
        response.status_code = 404
        return response

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
        return create_paciente()

@paciente_controller.route(f'/{module_name}/atualizar/', methods = ['POST'])
def get_atualizar_paciente():
    return atualizar_paciente()

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

    results = buscar_paciente(**params)
    return results
#
# @paciente_controller.route(f'/{module_name}/deletar/', methods = ['DELETE'])
# def delete_paciente():
#     cpf = request.args.get('cpf')
#     results = delete_paciente(cpf)
#     return results