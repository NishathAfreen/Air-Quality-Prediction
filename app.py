from flask import Flask, render_template, request
from sklearn.preprocessing import StandardScaler
import jsonify
import requests
import pickle
import numpy as np
import sklearn
app = Flask(__name__)
model = pickle.load(open('majorproject.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')
standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        SO2 = float(request.form['SO2'])
        NO2=float(request.form['NO2'])
        Particulate_Matter=float(request.form['Particulate_Matter'])
        O3=float(request.form['O3'])
        NO=float(request.form['NO'])
        NOx=float(request.form['NOx'])
        NH3=float(request.form['NH3'])
        prediction=model.predict([[SO2,NO2,Particulate_Matter,O3,NO,NOx,NH3]])
        output=prediction
        return render_template('index.html',prediction_text="AQI Range is {}".format(output[0]))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
