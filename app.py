import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from flask import Flask,request,jsonify,render_template


application=Flask(__name__)
app=application

#import ridge regressor and standaerd scaler pickle
ridge_model=pickle.load(open('models/ridge.pkl','rb'))
standard_scaler=pickle.load(open('models/scaler.pkl','rb'))


@app.route("/")
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=="POST":
        Temperature=float(reuest.form.get('Temperature'))
        RH=float(reuest.form.get('RH'))
        Ws=float(reuest.form.get('Ws'))
        Rain=float(reuest.form.get('Rain'))
        FFMC=float(reuest.form.get('FFMC'))
        DMC=float(reuest.form.get('DMC'))
        ISI=float(reuest.form.get('ISI'))
        Classes=float(reuest.form.get('Classes'))
        Region=float(reuest.form.get('Region'))

        new_data_scaled=standard_scaler.transform([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
        result=ridge_model.predict(new_data_scaled)

        return render_template('home.html',results=result[0 ])
    else:
        return render_template('home.html')    

if __name__=="__main__":
    app.run(host="0.0.0.0")