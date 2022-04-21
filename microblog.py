from app import app
import os
"""
se for o main criar a variável PORT para que ele recupere no sistema operacional a porta local onde o servidor estará rodando. Se o Heroku não setar nenhuma, ele utilizará a porta 5000
"""
if __name__== 'main':
    port = int(os.getenv('PORT'), '5000')
    app.run(HOST='0.0.0.0', port = port)