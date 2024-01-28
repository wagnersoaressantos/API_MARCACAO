class Sus:

    def __init__(self , sus,paciente_id, data_inicio, data_final = None, id = None ):

        self.id = id
        self.numero_sus = sus
        self.paciente_id = paciente_id
        self.data_inicio = data_inicio
        self.data_final = data_final

    def __repr__(self):
        return f'paciente_id = {self.paciente_id}, sus = {self.numero_sus}, data_inicio = {self.data_inicio}, data_final = {self.data_final} '