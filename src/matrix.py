from haversine import haversine
from const import AVERAGE_SPEED

LAT = 0
LONG = 1 

def calculation( latInit, longInit, latFin, longFin):
    init = (latInit, longInit)
    fim = (latFin, longFin)

    distance = haversine(init, fim)
    duration = distance/AVERAGE_SPEED

    return {
        'distance': distance,
        'duration': duration
    }

def generation(data):
    distances = []
    travelTimes = []
    for origin in range( len(data) ):
        distancesLine = []
        travelTimesLine = []
        for destination in range( len(data) ):
            if(destination == 0):
                distancesLine.append(0.0)
                travelTimesLine.append(0.0)
            elif(origin == len(data)-1):
                distancesLine.append(0.0)
                travelTimesLine.append(0.0)
            else:
                value = calculation(float(data[origin][LAT].replace(',', '.')),float(data[origin][LONG].replace(',', '.')),float(data[destination][LAT].replace(',', '.')),float(data[destination][LONG].replace(',', '.')))
                distancesLine.append(value['distance'])
                travelTimesLine.append(value['duration'])

        distances.append(distancesLine)
        travelTimes.append(travelTimesLine)

    return {
        'distances':distances,
        'travelTimes':travelTimes
    }
