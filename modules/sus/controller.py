from datetime import datetime

from flask import Blueprint, jsonify, request
# from pip._internal.utils import datetime

from modules.paciente.dao import DAOPaciente
from modules.sus.dao import DAOSus
from modules.sus.modelo import Sus
from modules.sus.sql import SQLSus

dao_sus = DAOSus()
dao_paciente = DAOPaciente()
module_name = 'sus'

class ControllerSus:
    def create_sus(self,paciente_id, sus):
        sus_data = (paciente_id, sus)
        erros = []
        for data in sus_data:
            # print(data)
            for campo in SQLSus._CAMPOS_OBRIGATORIOS:
                if campo not in data.keys() or not data.get(campo, '').strip():
                    erros.append(f'O campo {campo} é obrigatorio')
            print('verificando se o SUS existe')
            if dao_paciente.get_by_sus(data.get(sus)):
                erros.append(f'Já existe um cadastro')

        print('verificando se o paciente existe')
        paciente = dao_paciente.get_by_id(paciente_id)

        if not paciente:
            raise ValueError("Paciente não encontrado!")

        historico = dao_sus.get_by_sus(paciente_id)

        if historico:
            data_final = datetime.strptime(sus['data_inicio'], "%Y-%m-%d")
            historico[0]['data_final'] = data_final.strftime("%Y-%m-%d")
        data_inicio_sus_novo = datetime.now().strftime("%Y-%m-%d")
        data_final_sus_novo = None

        sus_novo = Sus(paciente_id,sus,data_inicio_sus_novo,data_final_sus_novo)
        sus_novo = dao_sus.salvar(sus_novo)
        print("novo sus é: ",sus_novo)
        response = jsonify('Sus adicionado com sucesso!')
        response.status_code = 201
        return response

    def get_by_sus(self, sus):
        return DAOSus.get_by_sus(sus)