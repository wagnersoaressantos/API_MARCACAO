from modules.paciente.modelo import Paciente
from modules.paciente.sql import SQLPaciente
from service.connect import Connect


class DAOPaciente(SQLPaciente):
    def __init__(self):
        self.connection = Connect().get_instance()

    def create_table(self):
        return self._CREATE_TABLE

    def salvar(self, paciente: Paciente):
        if not isinstance(paciente, Paciente):
            raise Exception("Tipo inválido")
        query = self._INSERTO_INTO
        cursor = self.connection.cursor()
        cursor.execute(query,(paciente.nome, paciente.mae, paciente.pai, paciente.cpf, paciente.data_nasc))
        self.connection.commit()
        return paciente

    def get_all(self):
        query = self._SELECT_ALL
        cursor = self.connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cols = [desc[0] for desc in cursor.description]
        results = [dict(zip(cols, i)) for i in results]
        results = [Paciente(**i) for i in results]
        return results

    def get_by_nome(self, nome):
        query = self._SELECT_BY_NOME
        cursor = self.connection.cursor()
        cursor.execute(query, ('%'+nome+'%',))
        results = cursor.fetchall()
        if results:
            cols = [desc[0] for desc in cursor.description]
            results = [dict(zip(cols, i)) for i in results]
            results = [Paciente(**i) for i in results]
            return results
        else:
            return None

    def get_by_mae(self, mae):
        query = self._SELECT_BY_MAE
        cursor = self.connection.cursor()
        cursor.execute(query, ('%'+mae+'%',))
        results = cursor.fetchall()
        if results:
            cols = [desc[0] for desc in cursor.description]
            results = [dict(zip(cols, i)) for i in results]
            results = [Paciente(**i) for i in results]
            return results
        else:
            return None

    def get_by_cpf(self, cpf):
        query = self._SELECT_BY_CPF
        cursor = self.connection.cursor()
        cursor.execute(query, (cpf,))
        results = cursor.fetchall()
        if results:
            cols = [desc[0] for desc in cursor.description]
            results = [dict(zip(cols, i)) for i in results]
            results = [Paciente(**i) for i in results]
            return results
        else:
            return None

    def get_by_data_nasc(self, data_nasc):
        query = self._SELECT_BY_DATA_NASC
        cursor = self.connection.cursor()
        cursor.execute(query, (data_nasc,))
        results = cursor.fetchall()
        if results:
            cols = [desc[0] for desc in cursor.description]
            results = [dict(zip(cols, i)) for i in results]
            results = [Paciente(**i) for i in results]
            return results
        else:
            return None

    def get_id_by_cpf(self, cpf):
        query = self._SELECT_ID_BY_CPF
        cursor = self.connection.cursor()
        cursor.execute(query, (cpf,))
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            return None
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