# MongoDB

```python
client = MongoClient(URI)
db = client["CadernoReceitas"]
col = db["receitas"]
```

Inserir:

```python
r = col.insert_one({...})
str(r.inserted_id)
```

Buscar por id:

```python
from bson.objectid import ObjectId
col.find_one({"_id": ObjectId(id_str)})
```

Id inválido → tratar exceção e responder 404.
