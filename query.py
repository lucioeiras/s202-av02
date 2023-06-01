from config.database import Database

db = Database("bolt://18.215.14.216:7687", "neo4j", "title-date-boats")

# 1) a
query = "MATCH (t:Teacher {name: 'Renzo'}) RETURN t.ano_nasc AS ano_nasc, t.cpf AS cpf"
result = db.execute_query(query)
print(result) 

# 1) b
query = "MATCH (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name AS name, t.cpf AS cpf"
result = db.execute_query(query)
print(result) 

# 1) c
query = "MATCH (c:City) RETURN c.name AS name"
result = db.execute_query(query)
print(result) 

# 1) d
query = "MATCH (s:School) WHERE s.number >= 150 AND s.number <= 550 RETURN s.name AS name, s.address AS address, s.number AS number"
result = db.execute_query(query)
print(result) 

# 2) a
query = "MATCH (t:Teacher) RETURN t.ano_nasc AS ano_nasc ORDER BY t.ano_nasc"
result = db.execute_query(query)
print(result[0], result[len(result) - 1]) 

# 2) b
query = "MATCH (c:City) RETURN avg(c.population) AS media"
result = db.execute_query(query)
print(result) 

# 2) c
query = "MATCH (c:City) WHERE c.cep = '37540-000' RETURN replace(c.name, 'a', 'A') AS name"
result = db.execute_query(query)
print(result) 

# 2) d
query = "MATCH (t:Teacher) RETURN substring(t.name, 3, 1) AS name"
result = db.execute_query(query)
print(result) 