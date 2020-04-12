#data = {
 # "region":
  #{
   #   "name": "Africa",
    #  "avgAge": 19.7,
     ##"avgDailyIncomePopulation": 0.71
  #},
  #"periodType": "weeks",
  #"timeToElapse": 7,
  #"reportedCases": 784,
  #"population": 66622705,
  #"totalHospitalBeds": 1380614
#}




def days(data):
        availablebeds = data["totalHospitalBeds"]
        impact= {
              'currentlyInfected': data['reportedCases']* 10,
                }
        severeImpact = {
              'currentlyInfected': data['reportedCases']* 50,
              }
        impact['infectionsByRequestedTime'] = impact['currentlyInfected'] * pow(2, int(data['timeToElapse']/3))
        severeImpact['infectionsByRequestedTime'] = severeImpact['currentlyInfected'] * pow(2, int((data['timeToElapse']/ 3)))   
        impact['severeCasesByRequestedTime'] = int(0.15 * impact['infectionsByRequestedTime'])
        severeImpact['severeCasesByRequestedTime'] = int(0.15 * severeImpact['infectionsByRequestedTime'])
        impact['hospitalBedsByRequestedTime'] = int(availablebeds - impact['severeCasesByRequestedTime'])
        severeImpact['hospitalBedsByRequestedTime'] = int(availablebeds - severeImpact['severeCasesByRequestedTime'])
        impact['casesForICUByRequestedTime'] = int(0.05 * impact['infectionsByRequestedTime'])
        severeImpact['casesForICUByRequestedTime'] = int(0.05 * severeImpact['infectionsByRequestedTime'])
        impact['casesForVentilatorsByRequestedTime'] = int(0.02 * impact['infectionsByRequestedTime'])
        severeImpact['casesForVentilatorsByRequestedTime'] = int(0.02 * severeImpact['infectionsByRequestedTime'])
        impact['dollarsInFlight'] = int(impact['infectionsByRequestedTime'] * 0.65 * 1.5 / data['timeToElapse'])
        severeImpact['dollarsInFlight'] = int(severeImpact['infectionsByRequestedTime'] * 0.65 * 1.5 / data['timeToElapse'])
        result = {
          'data': data,
          'impact': impact,
          'severeImpact': severeImpact,
        }
        return result

def weeks(data):
        availablebeds = data["totalHospitalBeds"]
        impact = {
              'currentlyInfected': data['reportedCases']* 10,
                }
        severeImpact = {
              'currentlyInfected': data['reportedCases']* 50,
              }
        impact['infectionsByRequestedTime'] = impact['currentlyInfected'] * pow(2, int(data['timeToElapse']*7/3))
        severeImpact['infectionsByRequestedTime'] = severeImpact['currentlyInfected'] * pow(2, int(data['timeToElapse']*7 / 3))
        impact['severeCasesByRequestedTime'] = int(0.15 * impact['infectionsByRequestedTime'])
        severeImpact['severeCasesByRequestedTime'] = int(0.15 * severeImpact['infectionsByRequestedTime'])
        impact['hospitalBedsByRequestedTime'] = int(availablebeds - impact['severeCasesByRequestedTime'])
        severeImpact['hospitalBedsByRequestedTime'] = int(availablebeds - severeImpact['severeCasesByRequestedTime'])
        impact['casesForICUByRequestedTime'] = int(0.05 * impact['infectionsByRequestedTime'])
        severeImpact['casesForICUByRequestedTime'] = int(0.05 * severeImpact['infectionsByRequestedTime'])
        impact['casesForVentilatorsByRequestedTime'] = int(0.02 * impact['infectionsByRequestedTime'])
        severeImpact['casesForVentilatorsByRequestedTime'] = int(0.02 * severeImpact['infectionsByRequestedTime'])
        impact['dollarsInFlight'] = format(impact['infectionsByRequestedTime'] * 0.65 * 1.5 * data['timeToElapse'])
        severeImpact['dollarsInFlight'] = format(severeImpact['infectionsByRequestedTime'] * 0.65 * 1.5 * data['timeToElapse']*7)
        result = {
          "Data": data,
          "impact": impact,
          "severeImpact": severeImpact,
        }
        return result

def months(data):
        availablebeds = data["totalHospitalBeds"]
        impact = {
              'currentlyInfected': data['reportedCases']* 10,
                }
        severeImpact = {
              'currentlyInfected': data['reportedCases']* 50,
              }
        impact['infectionsByRequestedTime'] = impact['currentlyInfected'] * pow(2, int(data['timeToElapse']*30/ 3))
        severeImpact['infectionsByRequestedTime'] = severeImpact['currentlyInfected'] * pow(2, int(data['timeToElapse']*30 / 3))
        impact['severeCasesByRequestedTime'] = int(0.15 * impact['infectionsByRequestedTime'])
        severeImpact['severeCasesByRequestedTime'] = int(0.15 * severeImpact['infectionsByRequestedTime'])
        impact['hospitalBedsByRequestedTime'] = int(availablebeds - impact['severeCasesByRequestedTime'])
        severeImpact['hospitalBedsByRequestedTime'] = int(availablebeds - severeImpact['severeCasesByRequestedTime'])
        impact['casesForICUByRequestedTime'] = int(0.05 * impact['infectionsByRequestedTime'])
        severeImpact['casesForICUByRequestedTime'] = int(0.05 * severeImpact['infectionsByRequestedTime'])
        impact['casesForVentilatorsByRequestedTime'] = int(0.02 * impact['infectionsByRequestedTime'])
        severeImpact['casesForVentilatorsByRequestedTime'] = int(0.02 * severeImpact['infectionsByRequestedTime'])
        impact['dollarsInFlight'] = format(impact['infectionsByRequestedTime'] * 0.65 * 1.5 * data['timeToElapse'])
        severeImpact['dollarsInFlight'] = format(severeImpact['infectionsByRequestedTime'] * 0.65 * 1.5 * data['timeToElapse'] * 30)
        print(impact)
        result = {
          "data": data,
          "impact": impact,
          "severeImpact" : severeImpact
        }
        return result