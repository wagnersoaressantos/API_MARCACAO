class SQLPaciente:
    _COL_ID = 'id'
    _COL_PACIENTE_ID = 'paciente_id'
    _TABLE_NAME = 'paciente'
    _TABLE_SUS_HISTORICO = 'sus_historico'
    _COL_NOME = 'nome'
    _COL_MAE = 'mae'
    _COL_PAI = 'pai'
    _COL_SUS = 'sus'
    _COL_CPF = 'cpf'
    _COL_DATA_NASC = 'data_nasc'
    _COL_DATA_INICIO = 'data_inicio'
    _COL_DATA_FINAL = 'data_final'
    _CAMPOS_OBRIGATORIOS = [_COL_NOME,_COL_CPF,_COL_SUS,_COL_MAE,_COL_DATA_NASC]

    _CREATE_TABLE = f'CREATE TABLE IF NOT EXISTS {_TABLE_NAME}' \
                    f'(id serial primary key,' \
                    f'{_COL_NOME} varchar(255),' \
                    f'{_COL_MAE} varchar(255),' \
                    f'{_COL_PAI} varchar(255),' \
                    f'{_COL_CPF} varchar(14) unique,' \
                    f'{_COL_DATA_NASC} varchar(10));'

    _INSERTO_INTO = f'INSERT INTO {_TABLE_NAME}({_COL_NOME},{_COL_MAE}, {_COL_PAI}, {_COL_CPF}, {_COL_DATA_NASC}) values(%s,%s,%s,%s,%s) RETURNING id;'
    _UPDATE_PACIENTE = f'UPDATE {_TABLE_NAME} SET {_COL_NOME} = %s, {_COL_MAE} = %s, {_COL_PAI} = %s, {_COL_DATA_NASC} = %s WHERE {_COL_ID} = %s'
    _SELECT_BY_NOME = f'SELECT * from {_TABLE_NAME} where {_COL_NOME} ilike %s'
    _SELECT_BY_CPF = f'SELECT * from {_TABLE_NAME} where {_COL_CPF} ilike %s'
    _SELECT_BY_SUS = f'SELECT p.* from {_TABLE_NAME} p INNER JOIN {_TABLE_SUS_HISTORICO} h ON p.{_COL_ID} = h.{_COL_PACIENTE_ID} WHERE h.{_COL_SUS} ILIKE %s'
    _SELECT_BY_MAE = f'SELECT * from {_TABLE_NAME} where {_COL_MAE} ilike %s'
    _SELECT_BY_DATA_NASC = f'SELECT * from {_TABLE_NAME} where {_COL_DATA_NASC} ilike %s'
    _SELECT_ALL = f'SELECT * from {_TABLE_NAME}'
    _SELECT_BY_ID = f'SELECT * from {_TABLE_NAME} where {_COL_ID} = %s'
    _SELECT_SUS_HISTORICO = f'SELECT * from {_TABLE_SUS_HISTORICO}'