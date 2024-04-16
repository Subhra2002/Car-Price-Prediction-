from flask import Flask,render_template
import pandas as pd
import pickle


model = pickle.load(open('LinearRegression.pkl','rb'))
data = pd.read_csv('Clean_Car_data.csv')

app = Flask(__name__)

@app.route('/')
def index():
    companies=sorted(data['company'].unique())
    car_models=sorted(data['name'].unique())
    year=sorted(data['year'].unique())
    fuel_type=sorted(data['fuel_type'].unique())
    return render_template('index.html',companies = companies,car_models= car_models,years= year,fuel_types= fuel_type)


@app.route('/predict',methods=['POST'])
def predict():
    company = request.form.get('comapny')
    car_model = request.form.get('car_model')
    year = int(request.form.get('year'))
    fuel_type = request.form.get('fuel_type')
    kms_driven = int(request.form.get('kilo_driven'))

    print(company,car_model,year,fuel_type,kms_driven)
    prediction = model.predict(pd.DataFrame([[company,car_model,year,fuel_type,kms_driven]],columns=['name','company','year','kms_driven',fuel_type]))
    print(prediction)


if __name__ == '__main__':
    app.run(debug = True)