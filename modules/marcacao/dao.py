from modules.marcacao.modelo import Marcacao
from modules.marcacao.sql import SQLMarcacao
from service.connect import Connect


class DAOMarcacao(SQLMarcacao):
    def __init__(self):
        self.connection = Connect().get_instance()

    def create_table(self):
        return self._CREATE_TABLE

    def salvar(self, marcacao: Marcacao):
        if not isinstance(marcacao, Marcacao):
            raise Exception("Tipo inválido")
        query = self._INSERTO_INTO
        cursor = self.connection.cursor()
        cursor.execute(query,(marcacao.sus, marcacao.cpf, marcacao.id_demanda, marcacao.data_solicitacao, marcacao.data_marcacao))
        self.connection.commit()
        return marcacao

    def get_all(self):
        query = self._SELECT_ALL
        cursor = self.connection.cursor()
        cursor.execute(query)
        marcacoes = []
        results = cursor.fetchall()
        for result in results:
            marcacao = {
                'id': result[0],
                'sus': result[1],
                'cpf': result[2],
                'demanda': result[3],
                'data_solicitacao': result[4],
                'data_marcacao': result[5]
            }
            marcacoes.append(marcacao)
        return marcacoes

    def get_demanda_by_sus_cpf(self,id_demanda, sus, cpf):
        query = self._SELECT_BY_SUS_OR_CPF
        cursor = self.connection.cursor()
        cursor.execute(query, (sus, cpf, id_demanda,))
        marcacoes = []
        results = cursor.fetchall()
        for result in results:
            marcacao = {
                'demanda': result[0],
                'data_solicitacao': result[1]
            }
            marcacoes.append(marcacao)
        return marcacoes

    def pegar_id_solicitacao(self,id_demanda, sus, cpf):
        query = self._SELECT_ID_MARCACAO_BY_SUS_OR_CPF_DEMANDA
        cursor = self.connection.cursor()
        cursor.execute(query, (sus, cpf, id_demanda))
        marcacoes = []
        results = cursor.fetchall()
        for result in results:
            marcacao = {
                'id': result[0],
                'demanda': result[1],
                'data_solicitacao': result[2],
                'data_marcacao': result[3]
            }
            marcacoes.append(marcacao)
        return marcacoes

    def get_demanda_reprimida(self):
        query = self._LIST_DEMANDA_REPRIMIDA
        cursor = self.connection.cursor()
        cursor.execute(query)
        marcacoes = []
        results = cursor.fetchall()
        for result in results:
            marcacao = {
                'demanda': result[0],
                'data_solicitacao': result[1]
            }
            marcacoes.append(marcacao)
        return marcacoes

    def realizar_marcacao(self, id_solicitacao, data_marcacao):
        query = self._UPDATE_MARCACAO
        cursor = self.connection.cursor()
        cursor.execute(query, (data_marcacao, id_solicitacao,))
        self.connection.commit()
        return 'sucesso'

    def get_solicitacoes_all(self):
        query = self._LISTA_SOLICITACOES_POR_PACIENTE
        cursor = self.connection.cursor()
        cursor.execute(query)
        marcacoes = []
        results = cursor.fetchall()
        print(f'Resultado {results}')
        for result in results:
            marcacao = {
                'Paciente': result[0],
                'demanda': result[1],
                'data_solicitacao': result[2],
                'data_marcacao': result[3]
            }
            marcacoes.append(marcacao)
        return marcacoes

    def get_solicitacao_by_demanda(self, demanda_id):
        query = self._LISTA_SOLICITACOES_POR_DEMENDA
        cursor = self.connection.cursor()
        cursor.execute(query, (demanda_id,))
        marcacoes = []
        results = cursor.fetchall()
        print(f'Resultado {results}')
        for result in results:
            marcacao = {
                'cpf paciente': result[0],
                'demanda': result[1],
                'data_solicitacao': result[2],
                'data_marcacao': result[3]
            }
            marcacoes.append(marcacao)
        return marcacoes

    def get_solicitacao_by_cpf(self, cpf):
        query = self._LISTA_SOLICITACOES_POR_CPF
        cursor = self.connection.cursor()
        cursor.execute(query, (cpf,))
        marcacoes = []
        results = cursor.fetchall()
        print(f'Resultado {results}')
        for result in results:
            marcacao = {
                'cpf paciente': result[0],
                'demanda': result[1],
                'data_solicitacao': result[2],
                'data_marcacao': result[3]
            }
            marcacoes.append(marcacao)
        return marcacoes


    def get_solicitacao_by_sus(self, sus):
        query = self._LISTA_SOLICITACOES_POR_SUS
        cursor = self.connection.cursor()
        cursor.execute(query, (sus,))
        marcacoes = []
        results = cursor.fetchall()
        print(f'Resultado {results}')
        for result in results:
            marcacao = {
                'paciente': result[0],
                'demanda': result[1],
                'data_solicitacao': result[2],
                'data_marcacao': result[3]
            }
            marcacoes.append(marcacao)
        return marcacoes