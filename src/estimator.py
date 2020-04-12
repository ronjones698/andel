from periodtype import (data, days, weeks, months, ptype, severeImpact, impact)
from flask_restful import Resource, Api
from flask import Flask, request,jsonify

app = Flask(__name__)
api = Api(app)


def estimator(data):
    if (str(ptype) == 'days'):
        days()
    elif (str(ptype) == 'weeks'):
        weeks()
    else:
        months()
    results = {
      'Data': data,
      'Impact': impact,
      'SevereImpact':severeImpact
    }
    return results

class RestAPI(Resource):
  def get(self):
    x = estimator(data)
    return x


api.add_resource(RestAPI,'/')

if __name__ == "__main__":
    app.run(debug=True)
#estimator(data)
