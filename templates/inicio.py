#bibliotecas
from flask import Flask
from flask import render_template

#creacion de rutas
app = Flask(__name__)

#/ se utiliza para la página principal
@app.route('/index')
def inicio():
    return render_template('index.html')


#ctrl+shift+r sirve para recargar sin cache
if __name__ == '__main__':
    app.run(debug = True)
