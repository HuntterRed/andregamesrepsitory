from fastapi import FastAPI

app = FastAPI()

jogos = [
    { 'nome': 'Hollow knight', 'genero': 'Ação'},
    { 'nome': 'Minecraft', 'genero': 'Aventura'}
]

@app.get('/games')
def list_games():
    return jogos