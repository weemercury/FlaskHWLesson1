from flask import Flask, make_response, redirect, render_template, request, url_for, session

app = Flask(__name__)
app.secret_key = '91ef658ddc76c8a4768e6bef94d6c617822d4eb0c6cc985264e5cda32ed9a098'


@app.route('/')
def index():
    if 'username' and 'email' in session:                  
        return redirect(url_for('hello'))
    else:
        return redirect(url_for('login'))       


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form.get('username')
        session['email'] = request.form.get('email') 
        return redirect(url_for('hello'))
    return render_template('task9.html')                        


@app.route('/hello/')
def hello():         
    return render_template('task9_hello.html')


@app.route('/logout/')
def logout():
    session.pop('username', None)  
    session.pop('email', None)                   
    return redirect(url_for('index'))


if __name__ == '__main__':  
    app.run(debug=True) 
   