from flask import Flask, request, render_template, redirect, url_for, abort
import logging

app = Flask(__name__)
logger = logging.getLogger(__name__)


@app.route('/')
def index():
        return f'Hello!'


@app.route('/task6', methods=['GET', 'POST'])
def task6():
    age = '18'
    if request.method == 'POST':
        if age == request.form.get('age'):
            return redirect(url_for('result'))
        else:
            return redirect(url_for('mistake'))
    return render_template('task6.html')


@app.route('/mistake/')
def mistake():
    return render_template('mistake1.html')


@app.route('/result/')
def result():
    context = {'age':'18'}
    return render_template('result.html', **context)


if __name__ == '__main__':  
    app.run(debug=True) 