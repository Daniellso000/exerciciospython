import MySQLdb 

con = MySQLdb.connect(host='localhost', user='root', passwd='dani112722', db = 'exercpython')

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
for c in id_usuario:
    cursor.execute(f"INSERT INTO final(id_usuario) VALUES ({c})")
    
for n in nomes:
    cursor.execute(f"INSERT INTO final(nome) VALUES ('{n}')")
    
for x in id_compra:
    cursor.execute(f"INSERT INTO final(id_compra) VALUES ({x})")

for z in valor:
    cursor.execute(f"INSERT INTO final(valor_compra) VALUES ({z})")

for b in item:
    cursor.execute(f"INSERT INTO final(item_compra) VALUES ('{b}')")

cursor.execute("SELECT * FROM final")

