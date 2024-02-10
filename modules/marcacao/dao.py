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
        print(results)
        for result in results:
            print(result)
            marcacao = {
                'id': result[0],
                'sus': result[1],
                'cpf': result[2],
                'demanda': result[3],
                'data_solicitacao': result[4],
                'data_marcacao': result[5]
            }
            marcacoes.append(marcacao)
            print(marcacao)

        return marcacoes
    #
    # def get_by_sus(self, sus):
    #     query = self._SELECT_SUS
    #     cursor = self.connection.cursor()
    #     cursor.execute(query, (sus,))
    #     results = cursor.fetchall()
    #     if results:
    #         sus_list = [sus[0] for sus in results]
    #         return sus_list
    #     else:
    #         return None
    #
    # def get_paciente_by_sus(self, sus):
    #     query = self._SELECT_PACIENTE_ID_BY_SUS
    #     cursor = self.connection.cursor()
    #     cursor.execute(query, (sus,))
    #     results = cursor.fetchall()
    #     if results:
    #         return results[0]
    #     else:
    #         return None
    #
    # def get_sus_by_paciente_id(self, paciente_id):
    #     query = self._SELECT_BY_SUS_ID
    #     cursor = self.connection.cursor()
    #     cursor.execute(query, (paciente_id,))
    #     results = cursor.fetchall()
    #     # print('result do get_by_sus_paciente_id: ', results[0])
    #     if results:
    #         sus_list = [sus[0] for sus in results]
    #         return sus_list
    #     else:
    #         return None
    #
    # def check_null_data_final(self, paciente_id):
    #     query = self._SELECT_NULL_DATA_FINAL
    #     cursor = self.connection.cursor()
    #     cursor.execute(query, (paciente_id,))
    #     results = cursor.fetchone()
    #     return results[0] > 0
    #
    # def list_sus_null_data_final(self, paciente_id):
    #     query = self._LIST_SUS_NULL_DATA_FINAL
    #     cursor = self.connection.cursor()
    #     cursor.execute(query, (paciente_id,))
    #     sus_list = cursor.fetchall()
    #     return sus_list
    #
    # def update_sus_null_data_final(self, sus, data_final):
    #     query = self._UPDATE_SUS
    #     cursor = self.connection.cursor()
    #     cursor.execute(query, (data_final, sus))
    #     self.connection.commit()
    #     return 'sucesso'
    #
    # def delete_sus_by_paciente_id(self, id):
    #     query = self._DELETE_BY_ID_PACIENTE
    #     cursor = self.connection.cursor()
    #     cursor.execute(query, (id,))
    #     self.connection.commit()
    #
    # def get_id_by_sus(self, sus):
    #     query = self._SELECT_ID_BY_SUS
    #     cursor = self.connection.cursor()
    #     cursor.execute(query, (sus,))
    #     result = cursor.fetchone()
    #     if result:
    #         return result[0]
    #     else:
    #         return None