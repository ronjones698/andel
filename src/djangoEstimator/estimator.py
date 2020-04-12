from periodtype import days,weeks,months


def estimator(data):

    ptype = data["periodType"]

    if (str(ptype) == 'days'):
        results = days(data)

    elif (str(ptype) == 'weeks'):
        results = weeks(data)

    else:
        results = months(data)

    return results



