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
                                  f'{_COL_DATA_INICIO} varchar(10),' \
                                  f'{_COL_DATA_FINAL} varchar(10),' \
                                  f'CONSTRAINT unique_sus_por_paciente UNIQUE ({_COL_SUS}, {_COL_PACIENTE_ID}));'

    _INSERTO_INTO = f'INSERT INTO sus_historico ({_COL_SUS}, {_COL_PACIENTE_ID}, {_COL_DATA_INICIO}, {_COL_DATA_FINAL}) values (%s, %s, %s, %s);'
    _UPDATE_SUS = f'UPDATE {_TABLE_NAME} SET {_COL_DATA_FINAL} = %s WHERE {_COL_SUS} = %s AND {_COL_DATA_FINAL} IS NULL;'
    _SELECT_PACIENTE_ID_BY_SUS = f'SELECT {_COL_PACIENTE_ID} from {_TABLE_NAME} WHERE {_COL_SUS} ILIKE %s'
    _SELECT_SUS = f'SELECT {_COL_SUS} from {_TABLE_NAME} WHERE {_COL_SUS} ILIKE %s'
    _SELECT_ALL = f'SELECT * from {_TABLE_NAME}'
    _SELECT_BY_SUS_ID = f'SELECT {_COL_SUS} from {_TABLE_NAME} WHERE {_COL_PACIENTE_ID} = %s'
    _SELECT_ID_BY_SUS = f'SELECT {_COL_ID} from {_TABLE_NAME} WHERE {_COL_SUS} = %s'
    _SELECT_NULL_DATA_FINAL = f'SELECT COUNT(*) FROM {_TABLE_NAME} WHERE {_COL_PACIENTE_ID} = %s AND {_COL_DATA_FINAL} IS NULL;'
    _LIST_SUS_NULL_DATA_FINAL = f'SELECT {_COL_SUS} FROM {_TABLE_NAME} WHERE {_COL_PACIENTE_ID} = %s AND {_COL_DATA_FINAL} IS NULL;'
    _DELETE_BY_ID_PACIENTE = f'DELETE FROM {_TABLE_NAME} WHERE {_COL_PACIENTE_ID} = %s'
