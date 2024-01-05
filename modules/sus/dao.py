from modules.sus.modelo import Sus
from modules.sus.sql import SQLSus
from service.connect import Connect


class DAOSus(SQLSus):
    def __init__(self):
        self.connection = Connect().get_instance()

    def create_table(self):
        return self._CREATE_TABLE

    def salvar(self, sus: Sus):
        if not isinstance(sus, Sus):
            raise Exception("Tipo inválido")
        query = self._INSERTO_INTO
        cursor = self.connection.cursor()
    #     cursor.execute(query,(paciente.nome, paciente.mae, paciente.pai, paciente.cpf, paciente.data_nasc))
    #     self.connection.commit()
    #
    #     # Verificar se tem resultado antes do paciente_id
    #     paciente_id = cursor.fetchone()[0]
    #     print("ID Paciente: ", paciente_id)
    #     self.adicionar_sus(paciente_id,paciente.sus)
    #     return paciente
    #
    # def adicionar_sus(self, paciente_id, novo_sus):
    #
    #     query_sus_historico = self._SELECT_SUS_HISTORICO
    #     cursor = self.connection.cursor()
    #     cursor.execute(query_sus_historico, (paciente_id,))
    #     sus_historico = cursor.fetchall()
    #     print(f"SUS Histórico antes da inserção: {sus_historico}")
    #
    #     # Adiciona SUS ao histórico
    #     query_insert_sus_historico = self._INSERT_SUS_HISTORICO
    #     cursor.execute(query_insert_sus_historico, (novo_sus, paciente_id))
    #     self.connection.commit()
    #
    #     # Recupera o novo histórico SUS para o paciente
    #     cursor.execute(query_sus_historico, (paciente_id,))
    #     novo_sus_historico = cursor.fetchall()
    #     print(f"SUS Histórico depois da inserção: {novo_sus_historico}")
    #
    #     return novo_sus_historico
    #
    # def get_by_sus(self, sus):
    #     query = self._SELECT_BY_SUS
    #     cursor = self.connection.cursor()
    #     cursor.execute(query, (sus,))
    #     results = cursor.fetchall()
    #     cols = [desc[0] for desc in cursor.description]
    #     results = [dict(zip(cols, i)) for i in results]
    #     results = [Paciente(**i) for i in results]
    #     return results
    #
    # def get_by_cpf(self, cpf):
    #     query = self._SELECT_BY_CPF
    #     cursor = self.connection.cursor()
    #     cursor.execute(query, (cpf,))
    #     results = cursor.fetchall()
    #     cols = [desc[0] for desc in cursor.description]
    #     results = [dict(zip(cols, i)) for i in results]
    #     results = [Paciente(**i) for i in results]
    #     return results
    #
    # def get_by_id(self, paciente_id):
    #     query = self._SELECT_BY_ID
    #     cursor = self.connection.cursor()
    #     cursor.execute(query, (paciente_id,))
    #     results = cursor.fetchone()
    #     if results:
    #         cols = [desc[0] for desc in cursor.description]
    #         results = dict(zip(cols, results))
    #         results = Paciente(**results)
    #         return results
    #     else:
    #         return None
    #
    # def get_all(self):
    #     query = self._SELECT_ALL
    #     cursor = self.connection.cursor()
    #     cursor.execute(query)
    #     results = cursor.fetchall()
    #     cols = [desc[0] for desc in cursor.description]
    #     results = [dict(zip(cols, i)) for i in results]
    #     results = [Paciente(**i) for i in results]
    #     return results