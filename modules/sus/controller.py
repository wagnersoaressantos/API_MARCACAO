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
module_name = 'sus'

class ControllerSus:

    def pegar_dados(self):
        dados = request.json
        erros = []
        for data in dados:
            for campo in SQLSus._CAMPOS_OBRIGATORIOS:
                if campo not in data.keys() or not data.get(campo, '').strip():
                    erros.append(f'O campo {campo} é obrigatorio')
            if dao_sus.get_by_sus(data.get("sus")):
                erros.append(f'Este sus já tem cadastro')
            if not data.get('cpf', '').strip():
                erros.append(f'O campo cpf é obrigatorio')
            if erros:
                response = jsonify(erros)
                response.status_code = 401
                return response
            paciente_id = comuns_controller.get_id_paciente_by_cpf(data.get('cpf'))
            if not paciente_id:
                response = jsonify('paciente não encontrado ou sem cadastro')
                response.status_code = 404
                return response
            sus_novo = data.get('sus')
            self.create_sus(paciente_id, sus_novo)
        response = jsonify('sucesso')
        response.status_code = 201
        return response

    def create_sus(self, paciente_id, sus_novo):
        historico = dao_sus.get_sus_by_paciente_id(paciente_id)
        if historico:
            dataInicio = datetime.now().strftime("%d/%m/%Y")
            dataFinal = dataInicio
            self.update_data_final_if_null(paciente_id, dataFinal)
            data_final_sus_novo = None
            sus_novo = Sus(sus_novo, paciente_id,dataInicio,data_final_sus_novo)
            dao_sus.salvar(sus_novo)
            response = jsonify('Sus adicionado com sucesso!')
            response.status_code = 201
            return response
        dataInicio = datetime.now().strftime("%d/%m/%Y")
        data_final_sus_novo = None
        sus_novo = Sus(sus_novo, paciente_id, dataInicio, data_final_sus_novo)
        dao_sus.salvar(sus_novo)
        response = jsonify('Sus adicionado com sucesso!')
        response.status_code = 201
        return response

    def update_data_final_if_null(self, paciente_id, nova_data_final):
        if dao_sus.check_null_data_final(paciente_id):
            sus_list = dao_sus.list_sus_null_data_final(paciente_id)
            for sus in sus_list:
                dao_sus.update_sus_null_data_final(sus, nova_data_final)
            return
        return

    def delete_sus(cpf):
        id = comuns_controller.get_id_paciente_by_cpf(cpf)
        if not id:
            response = jsonify({"message":"Paciente não encontrado!"})
            response.status_code = 404
            return response
        dao_sus.delete_sus_by_paciente_id(id)
        response = jsonify({"message": "Paciente e SUS deletado com sucesso!"})
        response.status_code = 200
        return response

    def get_sus(self):
        sus_all = dao_sus.get_all()
        results = [sus.__dict__ for sus in sus_all]
        response = jsonify(results)
        response.status_code = 200
        return response
    def get_sus_by_paciente_id(self, paciente_id):
        sus_list = dao_sus.get_sus_by_paciente_id(paciente_id)
        return sus_list

    def get_paciente_by_sus(self, sus):
        return dao_sus.get_paciente_by_sus(sus)

    def listar_sus_ou_pegar_id_paciente(self,sus = None):
        if sus:
            return dao_sus.get_paciente_by_sus(sus)
        return self.get_sus()

# @sus_controller.route(f'/{module_name}/', methods=['GET', 'POST'])
# def get_or_create_sus(self):
#     if request.method == 'GET':
#         return self.get_sus()
#     else:
#         return self.pegar_dados()
#
# @sus_controller.route(f'/{module_name}/buscar/', methods=['GET'])
# def get_buscar_sus(self):
#     sus = request.args.get('sus')
#     # cria um dicionario
#     params = {'sus': sus}
#     # params = {chave: valor for chave, valor in params.items() if valor is not None}
#     results = self.buscar_sus(**params)
#     return results