import psycopg2




class Connect:
    def __init__(self):
        config = dict(
            dbname = "controle_de_solicitacao",
            user="postgres", password="redgaw",
            host="localhost", port="5432"
        )
        self._connection = psycopg2.connect(**config)



    def create_tables(self):
        from modules.demanda.dao import DAODemanda
        from modules.paciente.dao import DAOPaciente
        cursor = self._connection.cursor()
        cursor.execute(DAOPaciente().create_table())
        cursor.execute(DAOPaciente().create_table_historico_sus())
        cursor.execute(DAODemanda().create_table())
        self._connection.commit()
        cursor.close()

    def get_instance(self):
        return self._connection