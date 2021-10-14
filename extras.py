from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse
import pickle
from preprocessing import WebContentPreprocessor
import pandas as pd

app = Flask(__name__)
api = Api(app)

# models
dt_model = pickle.load(open('decisiontree.pkl', 'rb'))
# knn_model = pickle.load(open('web-phishing-detection-using-knn.pkl', 'rb'))
# nb_model = pickle.load(open('naive-bayes.pkl', 'rb'))
# lr_model = pickle.load(open('lr-detection-model.pkl', 'rb'))



url_query_args = reqparse.RequestParser()
url_query_args.add_argument("url", type=str, help="Provide valid url", required=True)

# Load ML model
# Create a route
# Prepare data
# Run prediction
# Post processiong
# Return result
# processor = WebContentPreprocessor()

custom_feature = dict()

feature_state = {
    'legitimate': 1,
    'suspicious': 0,
    'phisheed': -1
}

# class ModelLayer(Resource):
#     def get(self):
        
#         # feature = [23, 1]
#         # prediction = model.predict([feature])
#         # print(prediction)
#         # return '', 200
#         return '', 200

#     def post(self):
#         # args = url_query_args.parse_args()
#         # state = processor.age_of_domain(args['url'])
#         # custom_feature['age_domain_'] = feature_state[state]
#         # processor.having_ip_address(args['url'])
#         # print(custom_feature)
#         new_data = [WebContentPreprocessor(1, -1, 0, 0, -1, 0, -1, 1, 0)]
#         df = pd.DataFrame([t.__dict__ for t in new_data])

#         prediction = dt_model.predict(df.values)
#         print(prediction)
#         return '', 200

# api.add_resource(ModelLayer, '/predict')
def dt_prediction():
    return

def knn_predict():
    return

def naive_bayes_predict():
    return

def logistic_reg_predict():
    return

@app.route('/welcome', methods=['GET'])
def welome_user():
    return jsonify({ 'message': 'welcome'})

@app.route('/analyze', methods=['POST'])
def analyze_url():
    print('hey')
    return jsonify(request.json)



if __name__ == "__main__":
    app.run(debug=True)


# incase
# new_data = [WebContentPreprocessor(1, -1, 0, 0, -1, 0, -1, 1, 0)]
