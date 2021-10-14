from flask import Flask, json, request, jsonify
from flask_restful import Api, Resource, reqparse
import pickle
from preprocessing import WebContentPreprocessor
import pandas as pd
import json

app = Flask(__name__)
api = Api(app)

df = pd.read_csv('datasets/phishtanksites.csv')
phised_sites = df['url'].values

# models
dt_model = pickle.load(open('models/decisiontree.pkl', 'rb'))
knn_model = pickle.load(open('models/knn_model.pkl', 'rb'))
nb_model = pickle.load(open('models/naive_bayes.pkl', 'rb'))
lr_model = pickle.load(open('models/logistics_regression.pkl', 'rb'))

url_query_args = reqparse.RequestParser()
url_query_args.add_argument("url", type=str, help="Provide valid url", required=True)


feature_state = {
    'legitimate': 1,
    'suspicious': 0,
    'phisheed': -1
}

@app.route('/resolveUrl', methods=['GET'])
def welome_user():
    return jsonify('welcome')

@app.route('/analyze', methods=['POST'])
def analyze_url():
    data = json.loads(request.data)

    parsed_url = data['url']
    if parsed_url in phised_sites:
        print('site is phished')
        return jsonify({ 'data': 'Phished' })

    dt_prediction = dt_model.predict([ [ 1, -1, 0, 0, -1, 0, -1, 1, 0 ] ])
    nb_prediction = nb_model.predict([ [ 1, -1, 0, 0, -1, 0, -1, 1, 0 ] ])
    # knn_prediction = knn_model([ [ 1, -1, 0, 0, -1, 0, -1, 1, 0 ] ])
    lr_prediction = lr_model.predict([ [ 1, -1, 0, 0, -1, 0, -1, 1, 0 ] ])

    # print(dt_prediction.accuracy_score())

    print('pred ', dt_prediction, nb_prediction, lr_prediction)

    if dt_prediction[0] == 1:
        return jsonify(data='legitimate')
    elif dt_prediction[0] == 0:
        return jsonify({ 'data': 'suspicious' })
    else:
        return jsonify({ 'data': 'phished' })

if __name__ == "__main__":
    app.run(debug=True)

