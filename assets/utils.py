import pymssql

def insert_banco(dados):
    conn = pymssql.connect(server='', user='', password='', database='')
    cursor = conn.cursor()

    sql_insert = """
        INSERT INTO ENDERECO (cep, logradouro, complemento, bairro, localidade, uf, ibge, gia, ddd, siafi)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql_insert, (
        dados['cep'],
        dados['logradouro'],
        dados.get('complemento', None),
        dados['bairro'],
        dados['localidade'],
        dados['uf'],
        dados['ibge'],
        dados['gia'],
        dados['ddd'],
        dados['siafi']
    ))
    conn.commit()
    cursor.close()
    conn.close()

 