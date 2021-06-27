#!python
#-*- coding: UTF-8 -*-

from bottle import run, request, post, get, template, route

@get('/')
def index():
    # data = request.body.read()
    print("asdertyyy") 
    return "asdertyyy"

@get('/api')
def api():
    # data = request.body.read()
    print("apiresponse") 
    return "apiresponse"

@route('/hello/<name>')
def greet(name='Stranger'):
    return template('Hello {{name}}, how are you?', name=name)

@post('/recv')
def recv():
    data = request.body.read()
    print(data) 

## matches /follow/defnull
@route('/<action>/<user>')         
def user_api(action, user):
    return template('action {{action}}, {{user}} user?', action=action, user=user )

@get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

def check_login(username,password):
    if (username == "admin" and password == "1234"):
        return True
    else:
        return False

@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"
 
run(host='0.0.0.0', port=8090, debug=True)
print("host=0.0.0.0 port=8090")
# run(host='0.0.0.0', port=8090, debug=True)