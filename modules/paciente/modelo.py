class Paciente():

    def __init__(self , nome, mae,sus,data_nasc, pai = None, id = None, cpf = None):
        self.id = id
        self.nome = nome
        self.mae = mae
        self.pai = pai
        self.sus = sus
        self.cpf = cpf
        self.data_nasc = data_nasc

    def __str__(self):
        pai_str = f'Pai: {self.pai}' if self.pai is not None else ''
        cpf_str = f'CPF: {self.cpf}' if self.cpf is not None else ''
        return 'Usuario: {} ' \
               'Mãe: {} ' \
               '{} ' \
               'SUS: {} ' \
               '{} ' \
               'Data de Nascimento: {}'.format(self.nome,self.mae,pai_str,self.sus,cpf_str,self.data_nasc)