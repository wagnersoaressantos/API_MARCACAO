from modules.paciente.modelo import Paciente
from modules.paciente.sql import SQLPaciente
from service.connect import Connect


class DAOPaciente(SQLPaciente):
    def __init__(self):
        self.connection = Connect().get_instance()

    def create_table(self):
        return self._CREATE_TABLE

    def create_table_historico_sus(self):
        return self._CREATE_SUS_HISTORICO_TABLE


    def salvar(self, paciente: Paciente):
        if not isinstance(paciente, Paciente):
            raise Exception("Tipo inválido")
        query = self._INSERTO_INTO
        cursor = self.connection.cursor()
        cursor.execute(query,(paciente.nome, paciente.mae, paciente.pai, paciente.cpf, paciente.data_nasc))
        self.connection.commit()

        # Verificar se tem resultado antes do paciente_id
        paciente_id = cursor.fetchone()[0]
        print("ID Paciente: ", paciente_id)
        self.adicionar_sus(paciente_id,paciente.sus)
        return paciente

    def adicionar_sus(self, paciente_id, novo_sus):
        # print(novo_sus)
        #         # adiciona SUS ao historic
        # query_sus = self._INSERT_SUS_HISTORICO
        # cursor = self.connection.cursor()
        # cursor.execute(query_sus,(novo_sus, paciente_id))
        # self.connection.commit()
        # return novo_sus
        # Recupera o histórico SUS para o paciente
        query_sus_historico = self._SELECT_SUS_HISTORICO
        cursor = self.connection.cursor()
        cursor.execute(query_sus_historico, (paciente_id,))
        sus_historico = cursor.fetchall()
        print(f"SUS Histórico antes da inserção: {sus_historico}")

        # Adiciona SUS ao histórico
        query_insert_sus_historico = self._INSERT_SUS_HISTORICO
        cursor.execute(query_insert_sus_historico, (novo_sus, paciente_id))
        self.connection.commit()

        # Recupera o novo histórico SUS para o paciente
        cursor.execute(query_sus_historico, (paciente_id,))
        novo_sus_historico = cursor.fetchall()
        print(f"SUS Histórico depois da inserção: {novo_sus_historico}")

        return novo_sus_historico

    def get_by_nome(self, nome):
        # query = self._SELECT_BY_NOME
        # with self.connection.cursor() as cursor:
        #     cursor.execute(query, (nome,))
        #     results = cursor.fetchall()
        #     cols = [desc[0] for desc in cursor.description]
        #     results = [dict(zip(cols, i)) for i in results]
        #     return [Paciente(**i) for i in results]

        query = self._SELECT_BY_NOME
        cursor = self.connection.cursor()
        cursor.execute(query, (nome,))
        results = cursor.fetchall()
        cols = [desc[0] for desc in cursor.description]
        results = [dict(zip(cols, i)) for i in results]
        results = [Paciente(**i) for i in results]
        return results

    def get_by_mae(self, mae):
        query = self._SELECT_BY_MAE
        cursor = self.connection.cursor()
        cursor.execute(query, (mae,))
        results = cursor.fetchall()
        cols = [desc[0] for desc in cursor.description]
        results = [dict(zip(cols, i)) for i in results]
        results = [Paciente(**i) for i in results]
        return results

    def get_by_data_nasc(self, data_nasc):
        query = self._SELECT_BY_DATA_NASC
        cursor = self.connection.cursor()
        cursor.execute(query, (data_nasc,))
        results = cursor.fetchall()
        cols = [desc[0] for desc in cursor.description]
        results = [dict(zip(cols, i)) for i in results]
        results = [Paciente(**i) for i in results]
        return results

    def get_by_sus(self, sus):
        query = self._SELECT_BY_SUS
        cursor = self.connection.cursor()
        cursor.execute(query, (sus,))
        results = cursor.fetchall()
        cols = [desc[0] for desc in cursor.description]
        results = [dict(zip(cols, i)) for i in results]
        results = [Paciente(**i) for i in results]
        return results

    def get_by_cpf(self, cpf):
        query = self._SELECT_BY_CPF
        cursor = self.connection.cursor()
        cursor.execute(query, (cpf,))
        results = cursor.fetchall()
        cols = [desc[0] for desc in cursor.description]
        results = [dict(zip(cols, i)) for i in results]
        results = [Paciente(**i) for i in results]
        return results

    def get_by_id(self, paciente_id):
        query = self._SELECT_BY_ID
        cursor = self.connection.cursor()
        cursor.execute(query, (paciente_id,))
        results = cursor.fetchone()
        if results:
            cols = [desc[0] for desc in cursor.description]
            results = dict(zip(cols, results))
            results = Paciente(**results)
            return results
        else:
            return None

    def get_all(self):
        query = self._SELECT_ALL
        cursor = self.connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cols = [desc[0] for desc in cursor.description]
        results = [dict(zip(cols, i)) for i in results]
        results = [Paciente(**i) for i in results]
        return results