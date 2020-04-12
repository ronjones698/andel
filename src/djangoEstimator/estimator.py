from periodtype import (days,weeks,months)

def estimator(data):
    ptype = data["periodType"]
    if (str(ptype) == 'Days'):
        x = days(data)
    elif (str(ptype) == 'Weeks'):
        x = weeks(data)
    else:
        x = months(data)
    return x


#estimator(data)
