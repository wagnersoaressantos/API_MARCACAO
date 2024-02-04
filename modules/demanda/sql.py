class SQLDemanda:
    _COL_ID = 'id'
    _TABLE_NAME = 'demanda'
    _COL_DEMANDA = 'demanda'
    _CAMPOS_OBRIGATORIOS = [_COL_DEMANDA]

    _CREATE_TABLE = f'CREATE TABLE IF NOT EXISTS {_TABLE_NAME}' \
                    f'(id serial primary key,' \
                    f'{_COL_DEMANDA} varchar(255));'

    _INSERTO_INTO = f'INSERT INTO {_TABLE_NAME}({_COL_DEMANDA}) values(%s)'
    _SELECT_BY_DEMANDA = f'SELECT * from {_TABLE_NAME} where {_COL_DEMANDA} ilike %s'
    _SELECT_ID_BY_DEMANDA = f'SELECT {_COL_ID} from {_TABLE_NAME} where {_COL_DEMANDA} ilike %s'
    _SELECT_ALL = f'SELECT * from {_TABLE_NAME}'
    _DELETE_BY_DEMANDA =f'DELETE from {_TABLE_NAME} where {_COL_DEMANDA} ilike %s'