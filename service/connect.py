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
        from modules.marcacao.dao import DAOMarcacao
        from modules.demanda.dao import DAODemanda
        from modules.paciente.dao import DAOPaciente
        from modules.sus.dao import DAOSus
        cursor = self._connection.cursor()
        cursor.execute(DAOPaciente().create_table())
        cursor.execute(DAOSus().create_table())
        cursor.execute(DAODemanda().create_table())
        cursor.execute(DAOMarcacao().create_table())
        self._connection.commit()
        cursor.close()

    def get_instance(self):
        return self._connection