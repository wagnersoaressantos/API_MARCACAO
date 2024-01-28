from datetime import datetime

from flask import Blueprint, jsonify, request

from modules.comuns.controller import ControllerComuns
# from pip._internal.utils import datetime

from modules.paciente.dao import DAOPaciente
from modules.sus.dao import DAOSus
from modules.sus.modelo import Sus
from modules.sus.sql import SQLSus

sus_controller = Blueprint('sus_controller', __name__)
comuns_controller = ControllerComuns()
dao_sus = DAOSus()
dao_paciente = DAOPaciente()
module_name = 'sus'

# class ControllerSus:
def pegar_dados():
    dados = request.json
    print('peganco os dados')
    print(dados)
    erros = []
    print('entrando no for para pegar os dados')
    for data in dados:
        print('no for',data)
        for campo in SQLSus._CAMPOS_OBRIGATORIOS:
            if campo not in data.keys() or not data.get(campo, '').strip():
                erros.append(f'O campo {campo} é obrigatorio')
        if dao_sus.get_by_sus(data.get('sus')):
            erros.append(f'Este sus já tem cadastro')
        if not data.get('cpf', '').strip():
            erros.append(f'O campo cpf é obrigatorio')
        if erros:
            response = jsonify(erros)
            response.status_code = 401
            print(response)
            return response

        paciente_id = comuns_controller.get_id_paciente_by_cpf(data.get('cpf'))
        print('id do paciente: ', paciente_id)
        if paciente_id:
            sus_novo = data.get('sus')
            print(f'solicitando adição do sus: {sus_novo} ao historico do sus')
            params = {'sus': sus_novo, 'paciente_id': paciente_id}
            print('params: ', params)
            create_sus(paciente_id, sus_novo)

            # dados_sus = sus_controller.create_sus(**params)
    #         print('dados adicionados: ', dados_sus)
    #     print(paciente)
    # response = jsonify('sucesso')
    # response.status_code = 201
    return jsonify('dados pegos!')

def create_sus(paciente_id=None, sus_novo=None):
    params = {'paciente_id': paciente_id, 'sus': sus_novo}
    print(params)
    sus_data = params
    print('em criar sus:',sus_data)
    print(f'verificando hitorico pelo id do paciente {paciente_id}')
    historico = dao_sus.get_by_sus_paciente_id(paciente_id)
    print('historico: ', historico)
    # if historico:
    #     print('No if do historico')
    #     print('historico do sus: ', historico)
    # print('pegando data para adicionar o sus ao historico')
    # dataInicio = datetime.now().strftime("%d/%m/%Y")
    # print('pegando data Inicio', dataInicio)
    # data_inicio_sus_novo = dataInicio
    # print(f'data inicial: {data_inicio_sus_novo}')
    # data_final_sus_novo = None
    # sus_novo = Sus(sus, paciente_id,data_inicio_sus_novo,data_final_sus_novo)
    # sus_novo = dao_sus.salvar(sus_novo)
    # print("novo sus é: ",sus_novo)
    # response = jsonify('Sus adicionado ecom sucesso!')
    response = jsonify('No create SUS!')
    response.status_code = 201
    return response

def get_sus():
    sus_all = dao_sus.get_all()
    results = [sus.__dict__ for sus in sus_all]
    response = jsonify(results)
    response.status_code = 200
    return response

def buscar_sus(sus = None):
    if sus:
        return get_by_sus(sus)
    return get_sus()
def get_by_sus(self, sus):
    sus_ = dao_paciente.get_by_nome(nome)
    if pacientes:
        results = [paciente.__dict__ for paciente in pacientes]
        response = jsonify(results)
        response.status_code = 200
        return response
    else:
        response = jsonify('nenhum resultado encontrado')
        response.status_code = 404
        return response

@sus_controller.route(f'/{module_name}/', methods=['GET', 'POST'])
def get_or_create_sus():
    if request.method == 'GET':
        return get_sus()
    else:
        return pegar_dados()

@sus_controller.route(f'/{module_name}/atualizar/', methods=['POST'])
def get_atualizar_paciente():
    return atualizar_paciente()

    # # def get_or_create_sus():
    # #    print("pegando sus sus")
    # #    if request.method == 'GET':
    # #        pass
    # #    else:
    # #        print("adicionando sus")
    # #        return sus_controller.create_sus()

    # @paciente_controller.route(f'/{module_name}/deletar/', methods=['DELETE'])
    # def delete_demanda():
    #     cpf = request.args.get('cpf')
    #     param = {'cpf': cpf}
    #     paciente = buscar_paciente(**param)
    #     print(paciente)
    #     results = delete_paciente(cpf)
    #     return results

    @sus_controller.route(f'/{module_name}/buscar/', methods=['GET'])
    def get_buscar_sus():
        sus = request.args.get('sus')

        # cria um dicionario
        params = {'sus': sus}
        # params = {chave: valor for chave, valor in params.items() if valor is not None}
        results = buscar_sus(**params)
        return results