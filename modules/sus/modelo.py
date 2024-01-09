class Sus:

    def __init__(self , numero_sus, data_inicio, paciente_id):
        self.paciente_id = paciente_id
        self.numero_sus = numero_sus
        self.data_inicio = data_inicio
        self.data_final = None

    def adicioner_ao_historico(self, data_final):
        self.data_final = data_final