import sqlite3

# Crie um banco de dados SQLite
conn = sqlite3.connect('populacao.db')
cursor = conn.cursor()

# Crie uma tabela para armazenar os dados de população
cursor.execute('''
    CREATE TABLE IF NOT EXISTS populacao (
        cidade TEXT,
        populacao INTEGER
    );
''')


# Insira alguns dados de exemplo
dados = [
    ('Fortaleza', 2701507),
    ('Caucaia', 362223),
    ('Juazeiro do Norte', 270383),
    ('Russas', 302234),
    ('Limoeiro', 226789),
    ('Quixere', 237789)
]

cursor.executemany('INSERT INTO populacao (cidade, populacao) VALUES (?, ?)', dados)

# Commit e feche o banco de dados
conn.commit()
conn.close()
