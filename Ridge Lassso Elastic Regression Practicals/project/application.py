from flask import Flask,request,jsonify,render_template
import pandas as pd
import numpy as np
import pickle 
app = Flask(__name__)

#import ridge regressor

ridgr_model = pickle.load(open('models/ridge.pkl' , 'rb'))
standard_scaler = pickle.load(open('models/scaler.pkl' , 'rb'))

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/predict' , methods =['GET' , 'POST'])
def perdict():
    if request.meth

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)