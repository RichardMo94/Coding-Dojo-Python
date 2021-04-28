# ---------------------#
from flask import Flask, render_template #Imports Flask to allow us to create our app
app = Flask(__name__) # Create a new instance of the Flask class called "app"
# ---------------------#

@app.route('/')
def hello_world():
    return render_template('index.html', phrase='hello', times=5) 

@app.route('/dojo')
def success():
    return 'Dojo!'

@app.route('/say/<name>')
def hello_person(name):
    return f"Hello {name}!!"

@app.route('/repeat/<times_repeat>/<word>')
def repeat(times_repeat,word):
    numRepeated = ''
    for i in range(int(times_repeat)):
        numRepeated += word+' '
    return numRepeated







# -------------------------#
if __name__=="__main__": # Ensure this file is being run directly and not from a different module 
    app.run(debug=True) # Run the app in debug mode.
# -------------------------#