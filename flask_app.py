
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import request, render_template
from fibonacci import fib, sumevenfib
import brainfuck
import sigil

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#STILL GUESSING
@app.route('/fib/')
def fib_default():
    return fib_results(100)

# UHHHH, just geussing.....
@app.route('/fib/<n>')
def fib_results(n):
    n2 = int(n)
    fib_results = str(fib(n2))
    alpha = str(sumevenfib(n2))
    return render_template('fibonacci.html',
        fib_results=fib_results, alpha=alpha)

@app.route('/bf/', methods=['GET','POST'])
def MyForm():
    result = ''
    if(request.method == 'POST'):
        result = brainfuck.run(request.form['text'])
    return render_template('brainfuck.html', result=result)

@app.route('/sig/', methods=['GET','POST'])
def SigilForm():
    answer = ''
    if(request.method == 'POST'):
        answer = sigil.Sigil_Aid(request.form['glyphs'])
    return render_template('sigil.html', result=answer)