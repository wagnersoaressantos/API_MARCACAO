class SQLSus:
    _COL_ID = 'id'
    _COL_PACIENTE_ID = 'paciente_id'
    _TABLE_NAME_PACIENTE = 'paciente'
    _TABLE_NAME = 'sus_historico'
    _COL_SUS = 'sus'
    _COL_DATA_INICIO = 'data_inicio'
    _COL_DATA_FINAL = 'data_final'
    _CAMPOS_OBRIGATORIOS = [_COL_SUS]

    _CREATE_TABLE = f'CREATE TABLE IF NOT EXISTS {_TABLE_NAME}' \
                                  f'(id serial PRIMARY KEY,' \
                                  f'{_COL_SUS} varchar(15) unique,' \
                                  f'{_COL_PACIENTE_ID} integer references {_TABLE_NAME}({_COL_ID}),' \
                                  f'{_COL_DATA_INICIO} TIMESTAMP DEFAULT CURRENT_TIMESTAMP,' \
                                  f'{_COL_DATA_FINAL} TIMESTAMP,' \
                                  f'CONSTRAINT unique_sus_por_paciente UNIQUE ({_COL_SUS}, {_COL_PACIENTE_ID}));'

    _INSERTO_INTO = f'INSERT INTO sus_historico ({_COL_SUS}, {_COL_PACIENTE_ID}, {_COL_DATA_INICIO}) values (%s, %s, %s);'
    _SELECT_BY_SUS = f'SELECT p.* from {_TABLE_NAME_PACIENTE} p INNER JOIN {_TABLE_NAME} h ON p.{_COL_ID} = h.{_COL_PACIENTE_ID} WHERE h.{_COL_SUS} ILIKE %s'
    _SELECT_ALL = f'SELECT * from {_TABLE_NAME}'