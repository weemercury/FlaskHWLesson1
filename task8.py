from flask import Flask, request, render_template, redirect, url_for, abort, flash
import logging


app = Flask(__name__)
app.secret_key = b'91ef658ddc76c8a4768e6bef94d6c617822d4eb0c6cc985264e5cda32ed9a098'
logger = logging.getLogger(__name__)


@app.route('/')
def index():
        return f'Hello!'


@app.route('/task8/', methods=['GET', 'POST'])
def task8():
    if request.method == 'POST':
        if not request.form['name']:               
            flash('Введите имя!', 'danger')         
            return redirect(url_for('task8'))
        flash(request.form['name'], 'success')
        return redirect(url_for('task8'))
    return render_template('task8.html')


if __name__ == '__main__':  
    app.run(debug=True) 