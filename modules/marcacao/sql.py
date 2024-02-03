class SQLMarcacao:
    _TABLE_NAME_PACIENTE = 'paciente'
    _TABLE_NAME_SUS = 'sus_historico'
    _TABLE_NAME_DEMANDA = 'demanda'
    _TABLE_NAME = 'marcacao'
    _COL_ID = 'id'
    _COL_PACIENTE_ID = 'paciente_id'
    _COL_SUS_ID = 'sus_id'
    _COL_DEMANDA_ID = 'demenda_id'
    _COL_DATA_SOLICITACAO = 'data_solicitação'
    _COL_DATA_MARCACAO = 'data_marcacao'
    _CAMPOS_OBRIGATORIOS = [_COL_DATA_SOLICITACAO,_COL_DEMANDA_ID,_COL_SUS_ID,_COL_PACIENTE_ID]

    _CREATE_TABLE = f'CREATE TABLE IF NOT EXISTS {_TABLE_NAME}' \
                    f'(id serial primary key,' \
                    f'{_COL_SUS_ID} varchar(150),' \
                    f'{_COL_PACIENTE_ID} varchar(150),' \
                    f'{_COL_DEMANDA_ID} varchar(150),' \
                    f'{_COL_DATA_SOLICITACAO} varchar(10),' \
                    f'{_COL_DATA_MARCACAO} varchar(10))'

    _INSERTO_INTO = f'INSERT INTO {_TABLE_NAME} ({_COL_SUS_ID}, {_COL_PACIENTE_ID}, {_COL_DEMANDA_ID}, {_COL_DATA_SOLICITACAO}, {_COL_DATA_MARCACAO}) values (%s, %s, %s, %s, %s);'
    _UPDATE_MARCACAO = f'UPDATE {_TABLE_NAME} SET {_COL_DATA_MARCACAO} = %s WHERE {_COL_SUS_ID} = %s AND {_COL_PACIENTE_ID} = %s AND {_COL_DATA_MARCACAO} IS NULL;'
    # _SELECT_PACIENTE_ID_BY_SUS = f'SELECT {_COL_PACIENTE_ID} from {_TABLE_NAME} WHERE {_COL_SUS} ILIKE %s'
    # _SELECT_SUS = f'SELECT {_COL_SUS} from {_TABLE_NAME} WHERE {_COL_SUS} ILIKE %s'
    # _SELECT_ALL = f'SELECT * from {_TABLE_NAME}'
    # _SELECT_BY_SUS_ID = f'SELECT {_COL_SUS} from {_TABLE_NAME} WHERE {_COL_PACIENTE_ID} = %s'
    # _SELECT_ID_BY_SUS = f'SELECT {_COL_ID} from {_TABLE_NAME} WHERE {_COL_SUS} = %s'
    # _SELECT_NULL_DATA_FINAL = f'SELECT COUNT(*) FROM {_TABLE_NAME} WHERE {_COL_PACIENTE_ID} = %s AND {_COL_DATA_FINAL} IS NULL;'
    # _LIST_SUS_NULL_DATA_FINAL = f'SELECT {_COL_SUS} FROM {_TABLE_NAME} WHERE {_COL_PACIENTE_ID} = %s AND {_COL_DATA_FINAL} IS NULL;'
    # _DELETE_BY_ID_PACIENTE = f'DELETE FROM {_TABLE_NAME} WHERE {_COL_PACIENTE_ID} = %s'
