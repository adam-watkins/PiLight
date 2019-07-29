from flask import Flask, render_template, request
import led

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form['state_button'] == 'On':
            led.on()
        elif request.form['state_button'] == 'Off':
            led.off()
        elif request.form['state_button'] == 'Red':
            led.colour('Red')
        elif request.form['state_button'] == 'Blue':
            led.colour('Blue')
        elif request.form['state_button'] == 'Green':
            led.colour('Green')
        elif request.form['state_button'] == 'Fade':
            led.fade()
    return render_template('index.html')


# Sever Run
app.run('0.0.0.0')
