from modules.demanda.modelo import Demanda
from modules.demanda.sql import SQLDemanda
from service.connect import Connect


class DAODemanda(SQLDemanda):
    def __init__(self):
        self.connection = Connect().get_instance()

    def create_table(self):
        return self._CREATE_TABLE

    def salvar(self, demanda: Demanda):
        if not isinstance(demanda, Demanda):
            raise Exception("Tipo inválido")
        query = self._INSERTO_INTO
        cursor = self.connection.cursor()
        cursor.execute(query,(demanda.demanda,))
        self.connection.commit()
        return demanda

    def get_by_demanda(self, demanda):
        query = self._SELECT_BY_DEMANDA
        cursor = self.connection.cursor()
        cursor.execute(query, (demanda,))
        results = cursor.fetchall()
        cols = [desc[0] for desc in cursor.description]
        results = [dict(zip(cols, i)) for i in results]
        results = [Demanda(**i) for i in results]
        return results

    def delete_by_demanda(self, demanda):
        query = self._DELETE_BY_DEMANDA
        cursor = self.connection.cursor()
        cursor.execute(query, (demanda,))
        self.connection.commit()
        return

    def get_id_by_demanda(self, demanda):
        query = self._SELECT_ID_BY_DEMANDA
        cursor = self.connection.cursor()
        cursor.execute(query, (demanda,))
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            return None

    # noinspection DuplicatedCode
    def get_all(self):
        query = self._SELECT_ALL
        cursor = self.connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cols = [desc[0] for desc in cursor.description]
        results = [dict(zip(cols, i)) for i in results]
        results = [Demanda(**i) for i in results]
        return results