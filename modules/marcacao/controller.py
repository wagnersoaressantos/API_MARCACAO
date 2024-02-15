from datetime import datetime
from flask import Blueprint, jsonify, request
from modules.comuns.controller import ControllerComuns
from modules.marcacao.dao import DAOMarcacao
from modules.marcacao.modelo import Marcacao
from modules.marcacao.sql import SQLMarcacao
# from modules.paciente.dao import DAOPaciente
# from modules.sus.dao import DAOSus
# from modules.sus.modelo import Sus
# from modules.sus.sql import SQLSus

marcacao_controller = Blueprint('marcacao_controller', __name__)
comuns_controller = ControllerComuns()
dao_marcacao = DAOMarcacao()
module_name = 'marcacao'

# class ControllerMarcacao:

def pegar_dados():
    global validador_sus
    dados = request.json
    erros = []
    for data in dados:
        for campo in SQLMarcacao._CAMPOS_OBRIGATORIOS:
            if campo not in data.keys() or not data.get(campo, '').strip():
                erros.append(f'O campo {campo} é obrigatorio')
            if not data.get('cpf', '').strip():
                erros.append(f'O campo cpf é obrigatorio')
            if not data.get('demanda', '').strip():
                erros.append(f'O campo demanda é obrigatorio')
            if not data.get('sus', '').strip():
                erros.append(f'O campo sus é obrigatorio')
            if not comuns_controller.get_id_sus_by_sus(data.get("sus")):
                erros.append(f'Sus não encontrado ou não existe')
            if erros:
                response = jsonify(erros)
                response.status_code = 401
                return response
        paciente_id = comuns_controller.get_id_paciente_by_cpf(data.get('cpf'))
        if not paciente_id:
            response = jsonify('paciente não encontrado ou sem cadastro')
            response.status_code = 404
            return response
        id_sus = comuns_controller.get_id_sus_by_sus(data.get('sus'))
        if not id_sus:
            response = jsonify('sus não encontrado ou sem cadastro')
            response.status_code = 404
            return response
        sus_cadastrado = comuns_controller.get_sus_by_paciente_id(paciente_id)
        for sus in sus_cadastrado:
            if sus == data.get('sus'):
                validador_sus = True
                break
            else:
                validador_sus = False
        if not validador_sus:
            response = jsonify('sus informado errado ou não pertence a esse paciente!')
            response.status_code = 404
            return response
        id_demanda = comuns_controller.get_id_demanda_by_demanda(data.get('demanda'))
        if not id_demanda:
            response = jsonify('Demanda não encontrada, foi informada errada ou não está cadastrada!')
            response.status_code = 404
            return response
        check_demanda = check_exist_demanda(id_demanda, data.get('sus'), data.get('cpf'))
        if check_demanda:
            marcacao_existente = True
            if marcacao_existente:
                resposta = input("Já existe uma marcação para esta demanda com datas diferentes. Deseja adicionar esta marcação? (sim/não): ")
                if resposta.lower() == 'sim':
                    # Aqui você prossegue com a adição da marcação
                    if 'data_solicitacao' in data:
                        if not data.get('data_solicitacao', '').strip():
                            create_solicitacao_marcacao(data.get('sus'), data.get('cpf'), id_demanda)
                        else:
                            create_solicitacao_marcacao(data.get('sus'), data.get('cpf'), id_demanda, data_solicitacao=data.get('data_solicitacao'))
                    return jsonify({'mensagem': 'Marcação adicionada com sucesso!'})
                elif resposta.lower() == 'não':
                    return jsonify({'mensagem': 'Marcação não adicionada.'})
                else:
                    return jsonify({'erro': 'Resposta inválida. Responda "sim" ou "não".'}), 400
            else:
                # Se não houver marcação duplicada, prossegue com a adição da marcação
                return jsonify({'mensagem': 'Marcação adicionada com sucesso!'})
        if 'data_solicitacao' in data:
            if not data.get('data_solicitacao', '').strip():
                result = create_solicitacao_marcacao(data.get('sus'), data.get('cpf'), id_demanda)
            else:
                result = create_solicitacao_marcacao(data.get('sus'), data.get('cpf'), id_demanda, data_solicitacao=data.get('data_solicitacao'))
        else:
            result = create_solicitacao_marcacao(data.get('sus'), data.get('cpf'), id_demanda)
        response = jsonify(result)
        response.status_code = 201
        return response


def create_solicitacao_marcacao(sus, cpf, demanda_id, data_solicitacao = None):

    if not data_solicitacao:
        data_solicitacao = datetime.now().strftime("%d/%m/%Y")
        marcacao = Marcacao(sus, cpf, demanda_id, data_solicitacao)
        dao_marcacao.salvar(marcacao)
    else:
        marcacao = Marcacao(sus, cpf, demanda_id, data_solicitacao)
        dao_marcacao.salvar(marcacao)
    return 'Solicitação adicionado com sucesso!'

def check_exist_demanda(id_demanda, sus, cpf):
    marcacoes = dao_marcacao.get_demanda_by_sus_cpf(id_demanda, sus, cpf)
    print(marcacoes)
    if marcacoes:
        return marcacoes
    else:
        return None

def get_marcacoes():
    marcacoes = dao_marcacao.get_all()
    response = jsonify(marcacoes)
    response.status_code = 200
    return response

def get_lista_demanda_reprimida():
    demanda_reprimida = dao_marcacao.get_demanda_reprimida()
    response = jsonify(demanda_reprimida)
    response.status_code = 200
    return response

@marcacao_controller.route(f'/{module_name}/', methods=['GET', 'POST'])
def get_or_create_marcacao():
    if request.method == 'GET':
        return get_marcacoes()
    else:
        return pegar_dados()

@marcacao_controller.route(f'/{module_name}/demanda/reprimida', methods=['GET'])
def get_demanda_reprimida():
        return get_lista_demanda_reprimida()