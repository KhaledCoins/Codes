"""Conexão com MongoDB Atlas — banco do caderno de receitas."""
from pymongo import MongoClient

URI = "mongodb+srv://USUARIO:SENHA@cluster0.xxxxx.mongodb.net/CadernoReceitas?retryWrites=true&w=majority"

client = MongoClient(URI)
db = client["CadernoReceitas"]
col_receitas = db["receitas"]
