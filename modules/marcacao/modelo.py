class Marcacao:

    def __init__(self , sus,cpf,id_demanda, data_solicitacao, data_marcacao = None, id = None ):

        self.id = id
        self.sus = sus
        self.cpf = cpf
        self.id_demanda = id_demanda
        self.data_solicitacao = data_solicitacao
        self.data_marcacao = data_marcacao
    def __repr__(self):
        return f'sus = {self.sus}, cpf = {self.cpf}, demanda = {self.id_demanda}, data solicitação = {self.data_solicitacao}, data marcacao = {self.data_marcacao}'