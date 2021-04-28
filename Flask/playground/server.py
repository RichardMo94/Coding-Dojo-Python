from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def index():
    return render_template('index.html', num=3)

@app.route('/play/<times>')
def repeat(times):
    return render_template('index.html', num=int(times))

@app.route('/play/<times>/<color>')
def color(times, color):
    return render_template('index.html', num=int(times), tempColor = color)

if __name__=='__main__':
    app.run(debug=True)