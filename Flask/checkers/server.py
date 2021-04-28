from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', num=4)

@app.route('/<someNum>')
def render(someNum):
    return render_template('index.html', num=int(someNum))

if __name__=="__main__":
    app.run(debug=True)