from modules.paciente.modelo import Paciente
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
        cursor.execute(query,(sus.numero_sus,sus.paciente_id,sus.data_inicio,sus.data_final))
        self.connection.commit()
        # Verificar se tem resultado antes do paciente_id
        paciente_id = cursor.fetchone()[2]
        print("ID Paciente: ", paciente_id)
        return sus

    def get_by_sus(self, sus):
        query = self._SELECT_BY_SUS
        cursor = self.connection.cursor()
        cursor.execute(query, (sus,))
        results = cursor.fetchall()
        cols = [desc[0] for desc in cursor.description]
        results = [dict(zip(cols, i)) for i in results]
        results = [Paciente(**i) for i in results]
        return results

    def get_by_sus_paciente_id(self, paciente_id):
        query = self._SELECT_BY_SUS
        cursor = self.connection.cursor()
        cursor.execute(query, (paciente_id,))
        results = cursor.fetchall()
        cols = [desc[0] for desc in cursor.description]
        results = [dict(zip(cols, i)) for i in results]
        results = [Paciente(**i) for i in results]
        return results