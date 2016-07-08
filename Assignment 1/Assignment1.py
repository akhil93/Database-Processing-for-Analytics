def generateInsert(table,attributes):
    '''
    >>> generateInsert('Students',['2','Alex,'A'])
    INSERT INTO Students VALUES ['2','Alex','A']
    '''
    query = 'INSERT INTO %s '%table + 'VALUES'
    values = []
    for k in attributes:
        values.append(str(k))
    query += ' ('+','.join(values)+') '
    return query