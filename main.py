from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)
todos = ['TODO1', 'TODO2', 'TODO3']


@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)

    return response


@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    # return 'Hello World su ip es {}'.format(user_ip)
    # return render_template('hello.html', user_ip=user_ip)
    context = {
        'user_ip' : user_ip,
        'todos' : todos,
    }

    return render_template('hello.html', **context)