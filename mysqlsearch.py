import MySQLdb 

con = MySQLdb.connect(host='localhost', user='root', passwd='', db = 'exercpython')

db_info = con.get_server_info()
print("Conectado com sucesso", db_info)
cursor = con.cursor()


cursor.execute("select * from usuarios")
linhas = cursor.fetchall()
nomes = []
item = []
valor = []
id_usuario = []
id_compra = []
for linha in linhas:
    nomes.append(linha[1])
cursor.execute("select * from compras")
linhas = cursor.fetchall()
for linha in linhas:
    item.append(linha[3])
    valor.append(linha[2])
    id_usuario.append(linha[1])
    id_compra.append(linha[0])

print(nomes)
print(item)
print(valor)
print(id_usuario)
print(id_compra)
