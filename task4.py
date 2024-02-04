from flask import Flask, request, render_template, redirect, url_for, abort
import logging

app = Flask(__name__)
logger = logging.getLogger(__name__)


@app.route('/')
def index():
        return f'Hello!'
    
    
@app.route('/task4', methods=['GET', 'POST'])
def task4():
    if request.method == 'POST':
        text = request.form.get('text')
        return str(len(text))
    return render_template('task4.html')
    
    

if __name__ == '__main__':  
    app.run(debug=True) 