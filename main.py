from flask import Flask, render_template, request
from datetime import datetime
from weather import predictWeather

# https://flask.palletsprojects.com/en/0.12.x/tutorial/templates/
# https://github.com/alanbanks229/flask_calculator_app/blob/master/calculator.py

app = Flask(__name__)

@app.route('/')
@app.route('/Weather/', methods = ['POST', 'GET'])
def weatherPage():
    predictedWeather = 3
    if request.method == 'POST':
        rf = request.form
        predictedWeather = predictWeather(int(rf.get('Month')), int(rf.get('Day')), int(rf.get('AveTemp')), int(rf.get('MaxTemp')), int(rf.get('MinTemp')), int(rf.get('WindDirect')), int(rf.get('WindSpeed'))).run()

    return render_template('Weather.html', weatherPred = predictedWeather)

if __name__ == "__main__":
   app.run()