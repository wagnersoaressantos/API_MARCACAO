from modules.demanda.dao import DAODemanda
from modules.paciente.dao import DAOPaciente

dao_demanda = DAODemanda()
dao_paciente = DAOPaciente()
dao_demanda = DAODemanda()
class ControllerComuns():
    def get_id_paciente_by_cpf(Self, cpf):
        id = dao_paciente.get_id_by_cpf(cpf)
        return id

    def get_id_demanda_by_demanda(Self, demanda):
        id = dao_demanda.get_id_by_demanda(demanda)
        return id

