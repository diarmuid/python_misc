from bottle import route, run, template
import os

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host=os.getenv('IP', '0.0.0.0') , port=os.getenv('PORT', 8080))