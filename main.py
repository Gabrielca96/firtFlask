from flask import Flask, request, make_response, redirect, render_template

#Almaceno en variable instancia de objeto flask
app = Flask(__name__)

todos = ['Comprar cafe', 'Compras', 'Vender']

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

# Decorador Pytho, Ruta raiz
# Método guarda ip de usuario en una cockie, para luego redirigir a ruta /hello 
@app.route('/')
def index():
    user_ip = request.remote_addr

    # make_response (variable de flask)
    response = make_response(redirect('/hello'))
    # Seteo una cookie que sera igual al ip del usuario
    response.set_cookie('user_ip', user_ip)

    # Regreso la respuesta
    return response

#Decorador python, ruta /hello
@app.route('/hello')
def hello():
    # obtengo ip de cockie oreviamente generada
    user_ip = request.cookies.get('user_ip')

    context = {
        'user_ip': user_ip,
        'todos': todos,
    }

    #Flask por defecto utiliza directorio template para renderizar html (from flask import render_template)
    return render_template('hello.html', **context)
