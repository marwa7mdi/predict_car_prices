from flask import Flask, render_template, request, redirect, make_response
import joblib

app = Flask(__name__)

model = joblib.load('./model/car_model.pkl')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/result/<int:result>", methods=["GET"])
def result(result):

    return render_template("result.html", result=result)

@app.route("/", methods=["POST"])
def predict():
    aspiration= request.form['aspiration']
    carbody = request.form['carbody']
    wheelbase =  request.form['wheelbase']
    carlength =  request.form['carlength']
    carwidth =  request.form['carwidth']
    carheight =  request.form['carheight']
    curbweight =  request.form['curbweight']
    enginesize =  request.form['enginesize']

    boreratio =  request.form['boreratio']
    stroke=request.form['stroke']
    compressionratio =  request.form['compressionratio']
    horsepower =  request.form['horsepower']
    peakrpm =  request.form['peakrpm']
    citympg =  request.form['citympg']
    highwaympg =  request.form['highwaympg']  
    
    result = int(round(model.predict([[aspiration,carbody, wheelbase, carlength, carwidth, carheight, curbweight, enginesize,  boreratio, stroke, compressionratio, horsepower, peakrpm, citympg, highwaympg]])[0]))
   # return render_template("result.html", result=result)
   # response = make_response()
   # response.headers['X-Parachutes'] = 'parachutes are cool'
    return redirect('/result/'+ str(result))




if __name__ == "__main__":
    app.run()
