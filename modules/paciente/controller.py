from flask import Blueprint, jsonify, request

from modules.paciente.dao import DAOPaciente
from modules.paciente.modelo import Paciente
from modules.paciente.sql import SQLPaciente

paciente_controller = Blueprint('paciente_controller', __name__)
dao_paciente = DAOPaciente()
module_name = 'paciente'

def get_paciente():
    pacientes = dao_paciente.get_all()
    results = [paciente.__dict__ for paciente in pacientes]
    response = jsonify(results)
    response.status_code = 200
    return response

def get_paciente_by_nome(nome):
    pacientes = dao_paciente.get_by_nome(nome)
    results = [paciente.__dict__ for paciente in pacientes]
    response = jsonify(results)
    response.status_code = 200
    return response

def get_paciente_by_mae(mae):
    pacientes = dao_paciente.get_by_mae(mae)
    results = [paciente.__dict__ for paciente in pacientes]
    response = jsonify(results)
    response.status_code = 200
    return response

def get_paciente_by_sus(sus):
    pacientes = dao_paciente.get_by_sus(sus)
    results = [paciente.__dict__ for paciente in pacientes]
    response = jsonify(results)
    response.status_code = 200
    return response

def get_paciente_by_cpf(cpf):
    pacientes = dao_paciente.get_by_cpf(cpf)
    results = [paciente.__dict__ for paciente in pacientes]
    response = jsonify(results)
    response.status_code = 200
    return response

def get_paciente_by_data_nasc(data_nasc):
    pacientes = dao_paciente.get_by_data_nasc(data_nasc)
    results = [paciente.__dict__ for paciente in pacientes]
    response = jsonify(results)
    response.status_code = 200
    return response

def create_paciente():
    pacientes = request.json
    print(pacientes)
    erros = []
    for data in pacientes:
        # print(data)
        for campo in SQLPaciente._CAMPOS_OBRIGATORIOS:
            if campo not in data.keys() or not data.get(campo, '').strip():
                erros.append(f'O campo {campo} é obrigatorio')
        print('verificando se o SUS existe')
        if dao_paciente.get_by_sus(data.get('sus')):
            erros.append(f'Já existe um cadastro')
        print('verificando se o cpf existe')
        if dao_paciente.get_by_cpf(data.get('cpf')):
            erros.append(f'já tem cadastro')
        if erros:
            response = jsonify(erros)
            response.status_code = 401
            print(response)
            return response

        paciente = Paciente(**data)
        paciente = dao_paciente.salvar(paciente)
        print(paciente)
    response = jsonify('sucesso')
    response.status_code = 201
    return response

def create_sus():
    pacientes = request.json
    print(pacientes)
    erros = []
    for data in pacientes:
        if dao_paciente.get_by_sus(data.get('sus')):
            erros.append(f'Já existe um cadastro')
        if erros:
            response = jsonify(erros)
            response.status_code = 401
            print(response)
            return response

        paciente = Paciente(**data)
        paciente = dao_paciente.adicionar_sus(paciente.id, paciente.sus)
        print(paciente)
    response = jsonify('sucesso')
    response.status_code = 201
    return response

def buscar_paciente(nome = None, mae = None, sus = None, data_nasc = None, cpf = None):

    if nome:
        return get_paciente_by_nome(nome)
    if mae:
        return get_paciente_by_mae(mae)
    if sus:
        return get_paciente_by_sus(sus)
    if data_nasc:
        return get_paciente_by_data_nasc(data_nasc)
    if cpf:
        return get_paciente_by_cpf(cpf)
    return get_paciente()


@paciente_controller.route(f'/{module_name}/', methods = ['GET', 'POST'])
def get_or_create_paciente():
    print("entrou get_or_create_paciente")
    if request.method == 'GET':
        return get_paciente()
    else:
        print("criar paciente")
        return create_paciente()

@paciente_controller.route(f'/{module_name}/addSUS/', methods = ['GET','POST'])
def get_or_create_sus():
   print("pegando sus sus")
   if request.method == 'GET':
       pass
   else:
       print("adicionando sus")
       return create_sus()

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

    results = [paciente.__dict__ for paciente in results]

    response = jsonify(results)
    response.status_code = 200
    return response
