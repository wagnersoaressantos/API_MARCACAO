class Marcacao:

    def __init__(self , id_sus,paciente_id,id_demanda, data_solicitacao, data_marcacao = None, id = None ):

        self.id = id
        self.id_sus = id_sus
        self.paciente_id = paciente_id
        self.id_demanda = id_demanda
        self.data_solicitacao = data_solicitacao
        self.data_marcacao = data_marcacao