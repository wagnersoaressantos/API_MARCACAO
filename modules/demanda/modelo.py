class Demanda():
    def __init__(self, demanda, id=None):
        self.id = id
        self.demanda = demanda

    def __str__(self):
        return 'Demanda: {}'.format(self.demanda)