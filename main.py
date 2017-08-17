from flask import Flask, request, redirect,render_template

app= Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def validate_user():
    username= request.form['username']
    password= request.form['password']
    verify= request.form['verify']
    email= request.form['email']

    username_error= ''
    password_error= ''
    verify_error= ''
    email_error= ''

    if username == '':
        username_error= 'Please enter a username'

    elif password == '':
        password_error= 'Please enter a password'

    if len(username) < 3 or len(username) > 20:
        username_error = 'Not a valid username'
        username = ''

    elif len(password) <3 or len(password) > 20:
        password_error = 'Not a valid password'
        password = ''

    if verify != password:
        verify_error = 'Passwords do not match'
        verify= ''

    if len(email)< 3 or len(email) > 20 or '@' not in email or "." not in email:
        email_error= 'Please enter a valid email'
        email= ''

    if not username_error and not password_error and not verify_error:
        return redirect ('/welcome?username={0}'.format(username))

    else:
        return render_template('index.html',username=username, email=email, username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error )

@app.route('/welcome')
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username= username)

app.run()
