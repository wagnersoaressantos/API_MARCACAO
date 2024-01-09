class Paciente():

    def __init__(self , nome, mae,data_nasc, pai = None, id = None, cpf = None):
        self.id = id
        self.nome = nome
        self.mae = mae
        self.pai = pai
        self.cpf = cpf
        self.data_nasc = data_nasc
        self.historico_sus = []

    def __str__(self):
        pai_str = f'Pai: {self.pai}' if self.pai is not None else ''
        cpf_str = f'CPF: {self.cpf}' if self.cpf is not None else ''
        return 'Usuario: {} ' \
               'Mãe: {} ' \
               '{} ' \
               'SUS: {} ' \
               '{} ' \
               'Data de Nascimento: {}'.format(self.nome,self.mae,pai_str,self.historico_sus,cpf_str,self.data_nasc)

    def adiciona_sus_no_historico(self, sus):
        self.historico_sus.append(sus)